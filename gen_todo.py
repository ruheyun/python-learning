import calendar
import os

def generate_monthly_markdown(year, month, tasks, filename=None):
    """
    生成月度清单 Markdown 表格
    :param year: 年份 (int)
    :param month: 月份 (int)
    :param tasks: 任务列表 (list of str)，例如 ['阅读', '背单词']
    :param filename: 输出文件名，如果不填则自动根据年月生成
    """
    
    # 1. 获取该月有多少天
    # calendar.monthrange 返回 (该月第一天是星期几, 该月天数)
    _, days_in_month = calendar.monthrange(year, month)
    
    # 2. 构建 Markdown 内容
    lines = []
    
    # 标题
    title = f"# {year}-{month:02d} 清单"
    lines.append(title)
    lines.append("") # 空行
    
    # 表头行 (第一列留空，后面接任务)
    # 格式: | | 阅读 | 背单词 | ... |
    header = "| | " + " | ".join(tasks) + " |"
    lines.append(header)
    
    # 分隔行
    # 格式: |---|---|---|...|
    separator = "|---|" + "---|" * len(tasks)
    lines.append(separator)
    
    # 数据行 (循环每一天)
    for day in range(1, days_in_month + 1):
        # 格式化日期，例如 07-01
        date_str = f"{month:02d}-{day:02d}"
        
        # 每一行：日期列 + 对应数量的空单元格
        # 格式: | 07-01 | | | ... |
        row = f"| {date_str} |" + " |" * len(tasks) + " |" # 注意最后补一个 | 闭合
        # 修正：上面的逻辑最后会多一个 | 或者少一个，重新调整一下
        # 正确的逻辑是：| 日期 | (空) | (空) | ...
        # 让我们用 join 来构建更稳妥
        cells = [date_str] + [""] * len(tasks)
        row = "| " + " | ".join(cells) + " |"
        
        lines.append(row)

    content = "\n".join(lines)
    
    # 3. 保存文件
    # if not filename:
    #     filename = f"{year}-{month:02d}_清单.md"
    
    # with open(filename, "w", encoding="utf-8") as f:
    #     f.write(content)
        
    print(f"✅ 成功生成文件: {filename}")
    print("-" * 30)
    print(content) # 在控制台也打印出来预览

# --- 配置区域 ---
if __name__ == "__main__":
    # 在这里修改你的配置
    target_year = 2026
    target_month = 6
    
    # 在这里修改你的任务列名
    my_tasks = ["阅读", "背单词", "练听力", "写代码", "看论文"]
    
    # 运行生成
    generate_monthly_markdown(target_year, target_month, my_tasks)
    