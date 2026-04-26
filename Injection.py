import json
import os
import re
import sys  # [新增] 引入sys模块用于获取命令行参数
from docxtpl import DocxTemplate, RichText

def str_to_richtext(text):
    """
    【终极版：嵌套富文本与颜色转换器】
    支持 <b>, <i>, <u> 以及预设颜色标签的任意嵌套组合。
    """
    # 允许的标签集合：加粗、斜体、下划线，以及颜色(r, g, bl, y, o, p)
    # 使用快筛正则以节省纯文本处理资源
    if not re.search(r'<(?:/?[biurgypo]|/?bl)>', text, re.IGNORECASE):
        return text
        
    rt = RichText()
    # 使用正则将字符串切分为 标签 和 文本片段
    parts = re.split(r'(<(?:/?[biurgypo]|/?bl)>)', text, flags=re.IGNORECASE)
    
    # 初始化样式状态表
    state = {'bold': False, 'italic': False, 'underline': False}
    color_stack = [] # 使用栈来支持颜色的完美嵌套
    
    # 颜色映射字典 (十六进制代码，不用加 #)
    color_map = {
        'r': 'FF0000',  # Red 红色
        'g': '00B050',  # Green 绿色
        'bl': '0070C0', # Blue 蓝色 (避开 b 加粗)
        'y': 'FFC000',  # Yellow 黄色
        'o': 'ED7D31',  # Orange 橙色
        'p': '7030A0'   # Purple 紫色
    }
    
    for part in parts:
        if not part:
            continue
        
        tag = part.lower()
        # 1. 处理加粗/斜体/下划线状态
        if tag == '<b>': state['bold'] = True
        elif tag == '</b>': state['bold'] = False
        elif tag == '<i>': state['italic'] = True
        elif tag == '</i>': state['italic'] = False
        elif tag == '<u>': state['underline'] = True
        elif tag == '</u>': state['underline'] = False
        
        # 2. 处理颜色开启标签 <r>, <g> 等
        elif tag.startswith('<') and not tag.startswith('</'):
            tag_name = tag[1:-1]
            if tag_name in color_map:
                color_stack.append(color_map[tag_name])
                
        # 3. 处理颜色闭合标签 </r>, </g> 等
        elif tag.startswith('</'):
            tag_name = tag[2:-1]
            if tag_name in color_map:
                if color_stack:
                    color_stack.pop() # 弹出当前颜色，恢复上一层颜色
                    
        # 4. 遇到实际文本，打包所有激活的样式进行渲染
        else:
            kwargs = {
                'bold': state['bold'],
                'italic': state['italic'],
                'underline': state['underline']
            }
            # 如果栈内有颜色，取最顶层的颜色生效
            if color_stack:
                kwargs['color'] = color_stack[-1]
                
            rt.add(part, **kwargs)
            
    return rt

def format_list_by_marker(raw_list):
    """
    【列表样式识别器】
    """
    if not raw_list:
        return ""
        
    first_item = str(raw_list[0]).strip()
    style = "n." 
    is_marker = False
    
    marker_mapping = {
        "n.": ["n.", "1.", "1", "1)", "(1)", "1、", "#"],
        "•": ["•", "·", "*", "●", "○", "°"],
        "-": ["-", "--", "—", "－"]
    }
    
    for canonical_style, aliases in marker_mapping.items():
        if first_item in aliases:
            style = canonical_style
            is_marker = True
            break
            
    if is_marker:
        items_to_process = raw_list[1:]
    else:
        items_to_process = raw_list
        
    valid_items = [str(i) for i in items_to_process if str(i).strip() != ""]
    
    if not valid_items:
        return ""
        
    if style == "n.":
        return "\n".join([f"{index + 1}. {item}" for index, item in enumerate(valid_items)])
    elif style == "•":
        return "\n".join([f"• {item}" for item in valid_items])
    elif style == "-":
        return "\n".join([f"- {item}" for item in valid_items])

def extract_x_variables(data, result_dict):
    """
    【递归扫描器】
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if isinstance(k, str) and k.startswith('x') and k[1:].isdigit():
                
                temp_val = "" 
                
                if v is None:
                    temp_val = ""
                elif isinstance(v, list):
                    temp_val = format_list_by_marker(v)
                elif isinstance(v, str) and "||" in v:
                    try:
                        segments = v.split("||")
                        processed_segments = []
                        for seg in segments:
                            seg = seg.strip()
                            if not seg:
                                continue
                            try:
                                parsed_data = json.loads(seg)
                                if isinstance(parsed_data, list):
                                    processed_segments.append(format_list_by_marker(parsed_data))
                                else:
                                    processed_segments.append(seg)
                            except ValueError:
                                processed_segments.append(seg)
                        temp_val = "\n\n".join(processed_segments)
                    except Exception:
                        temp_val = str(v)
                else:
                    temp_val = str(v)
                    
                result_dict[k] = str_to_richtext(temp_val)
                
            else:
                extract_x_variables(v, result_dict)
    elif isinstance(data, list):
        for item in data:
            extract_x_variables(item, result_dict)

def print_report(success, messages, output_file=None):
    """
    【终端运行报告生成器】
    """
    print("\n" + "="*50)
    print("【教学模板自动渲染引擎 - 运行报告】")
    print("="*50)
    
    if success:
        print("▶ 总体状态 : 成功 ✅")
        print(f"▶ 输出文件 : {output_file}")
    else:
        print("▶ 总体状态 : 失败 ❌ (流程已中断)")

    if messages:
        print("\n▶ 详细运行日志 (Warnings & Errors):")
        for i, msg in enumerate(messages, 1):
            prefix = "🚫" if "错误" in msg else "⚠️"
            print(f"  {prefix} {i}. {msg}")
    else:
        print("\n▶ 详细运行日志 : 完美运行，无任何缺失、报错或警告。")
    print("="*50 + "\n")

def main():
    # [修改开始]：动态获取输入输出路径
    if len(sys.argv) > 1:
        json_path = sys.argv[1]
    else:
        json_path = "LessonPlan.json"
        
    template_path = "References/Template.docx"
    
    # 截取 json 文件的命名来作为 docx 的命名
    base_name, _ = os.path.splitext(json_path)
    output_path = f"{base_name}.docx"
    # [修改结束]
    
    messages = []
    render_context = {}

    if not os.path.exists(template_path):
        messages.append(f"严重错误: 找不到模板文件 '{template_path}'，请检查路径。")
        print_report(False, messages)
        return

    if not os.path.exists(json_path):
        messages.append(f"严重错误: 找不到数据文件 '{json_path}'，请确认 Claude 是否已生成该文件。")
        print_report(False, messages)
        return

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        extract_x_variables(raw_data, render_context)
    except json.JSONDecodeError as e:
        messages.append(f"解析错误: {json_path} 文件格式损坏或不是合法的 JSON。细节: {str(e)}")
        print_report(False, messages)
        return
    except Exception as e:
        messages.append(f"未知读取错误: {str(e)}")
        print_report(False, messages)
        return

    missing_vars = []
    for i in range(1, 92):
        key = f"x{i:02d}"
        if key not in render_context:
            missing_vars.append(key)
            render_context[key] = "" 

    if missing_vars:
        messages.append(f"缺失警告: JSON 中未找到以下 {len(missing_vars)} 个占位符数据，已自动填为空白: {', '.join(missing_vars)}")

    try:
        doc = DocxTemplate(template_path)
        doc.render(render_context)
    except Exception as e:
        messages.append(f"渲染错误: 注入模板时发生异常。这通常是因为 Word 内部 XML 损坏。细节: {str(e)}")
        print_report(False, messages)
        return

    try:
        doc.save(output_path)
    except PermissionError:
        messages.append(f"保存错误: 文件 '{output_path}' 正被另一个程序（如 Word）打开。请关闭后重试！")
        print_report(False, messages)
        return
    except Exception as e:
        messages.append(f"保存错误: {str(e)}")
        print_report(False, messages)
        return

    print_report(True, messages, output_path)

if __name__ == "__main__":
    main()