"""
生成：模拟首次进场座谈记录 Word 文档
用途：xiaoyang-fusion v5.0 进化成果演示
输出：D:\Desktop\模拟座谈_建筑公司马总.docx
"""

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml
import datetime

doc = Document()

# ── 全局默认字体 ──
style = doc.styles['Normal']
font = style.font
font.name = '宋体'
font.size = Pt(14)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
pf = style.paragraph_format
pf.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
pf.first_line_indent = Cm(0.74)
pf.line_spacing = 1.5

# ── 辅助函数 ──

def add_heading_styled(text, level=1):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.name = '黑体'
        run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
        run.font.bold = True
        if level == 1:
            run.font.size = Pt(14)
        elif level == 2:
            run.font.size = Pt(14)
        elif level == 3:
            run.font.size = Pt(14)
    h.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h.paragraph_format.first_line_indent = Cm(0)
    return h

def add_body(text):
    p = doc.add_paragraph(text)
    return p

def add_body_bold(text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.name = '宋体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.font.size = Pt(14)
    return p

def add_quote(text):
    """灰色引文块"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(12)
    run.font.name = '宋体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
    run.italic = True
    p.paragraph_format.left_indent = Cm(1)
    p.paragraph_format.first_line_indent = Cm(0)
    return p

def add_dialogue(speaker, text, bold_speaker=True):
    """对话格式：小阳/马总"""
    p = doc.add_paragraph()
    run_s = p.add_run(f"{speaker}：")
    run_s.bold = bold_speaker
    run_s.font.name = '宋体'
    run_s.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run_s.font.size = Pt(14)
    run_t = p.add_run(text)
    run_t.font.name = '宋体'
    run_t.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run_t.font.size = Pt(14)
    return p

def add_mental_note(text):
    """心理活动/内功分析——灰色框"""
    p = doc.add_paragraph()
    run = p.add_run(f"🧠 {text}")
    run.font.size = Pt(12)
    run.font.name = '宋体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
    run.font.color.rgb = RGBColor(0x33, 0x66, 0x99)
    run.italic = True
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.first_line_indent = Cm(0)
    return p

def add_separator():
    p = doc.add_paragraph()
    run = p.add_run('─' * 40)
    run.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
    run.font.size = Pt(8)
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

def set_cell_shading(cell, color):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def add_table(headers, rows, col_widths=None):
    """添加格式化表格"""
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    # 设置表格宽度100%
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else parse_xml(f'<w:tblPr {nsdecls("w")}/>')
    tblW = parse_xml(f'<w:tblW {nsdecls("w")} w:w="5000" w:type="pct"/>')
    tblPr.append(tblW)

    # 表头
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.0
        run = p.add_run(h)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        run.font.name = '宋体'
        run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
        set_cell_shading(cell, '003366')

    # 数据行
    for ri, row in enumerate(rows):
        for ci, val in enumerate(row):
            cell = table.rows[ri + 1].cells[ci]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.0
            run = p.add_run(str(val))
            run.font.size = Pt(9)
            run.font.name = '宋体'
            run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
            cell.vertical_alignment = 1  # CENTER
            # 行高
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            trPr = table.rows[ri + 1]._tr.get_or_add_trPr()
            trHeight = parse_xml(f'<w:trHeight {nsdecls("w")} w:val="567" w:hRule="exact"/>')
            trPr.append(trHeight)
            # 隔行浅蓝
            if ri % 2 == 1:
                set_cell_shading(cell, 'F2F7FC')

    doc.add_paragraph()  # table spacing
    return table


# ═══════════════════════════════════════
# 封面
# ═══════════════════════════════════════

for _ in range(6):
    doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('模拟首次进场座谈记录')
run.bold = True
run.font.size = Pt(22)
run.font.name = '黑体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)

doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('xiaoyang-fusion v5.0 · 六源融合进化成果演示')
run.font.size = Pt(14)
run.font.name = '宋体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
run.font.color.rgb = RGBColor(0x66, 0x66, 0x66)

doc.add_paragraph()
doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('客户：马总 · 建筑公司（年营收3,000万）')
run.font.size = Pt(14)
run.font.name = '宋体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(f'编制：龙头会服高端财税服务团队')
run.font.size = Pt(14)
run.font.name = '宋体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run(f'日期：{datetime.date.today().strftime("%Y年%m月%d日")}')
run.font.size = Pt(14)
run.font.name = '宋体'
run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

doc.add_page_break()

# ═══════════════════════════════════════
# 前言
# ═══════════════════════════════════════

add_heading_styled('前言', level=1)

add_body(
    '本记录为财税顾问年度合同签约后第一次上门座谈的完整模拟推演。'
    '座谈全程遵循「首次进场尽调四步法」框架，同步启用 xiaoyang-fusion v5.0 新增的六项融合内功：'
)

items = [
    '五层消解漏斗（来源：dbs-diagnosis）——识别客户语言中的模糊词、错误假设、逻辑跳跃',
    '问题说明书五字段（来源：dbs-good-question）——把模糊需求钉成对象/目标/冲突/约束/反馈',
    '场景核心公式（来源：carnegie-influence）——说服、共情、推动行动等场景的公式化应对',
    '三级校验分级（来源：delivery-quality-check）——对话全程按P1级执行',
    '实战陷阱速查（来源：caishui-report-generator）——代账数据不可信、旧法数字陷阱等',
    '双场景交付判断（来源：messy-account-cleanup）——确认客户是正常经营而非注销',
]
for item in items:
    p = doc.add_paragraph(style='List Bullet')
    run = p.add_run(item)
    run.font.size = Pt(14)
    run.font.name = '宋体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')

add_body('全文灰色引文和蓝色标注为顾问在对话过程中同步进行的内部推理，不出声。')

doc.add_page_break()

# ═══════════════════════════════════════
# 正文
# ═══════════════════════════════════════

add_heading_styled('一、情景设定', level=1)
add_body('角色：小阳（财税顾问）对话马总（建筑公司老板）')
add_body('客户背景：年营收约3,000万元，主业市政工程+房建分包，有市政二级/房建三级资质，使用代账公司，妻子管钱。')
add_body('签约状态：年度财税顾问合同已签，今日为首次上门座谈。')

add_separator()

# ── 第1步 ──

add_heading_styled('二、第一步：对齐期望', level=1)

add_dialogue('小阳',
    '马总，合同签了，今天第一次来，主要想听听您的想法——'
    '您希望我们帮您达到什么效果？一年之后您希望公司是什么样的状态？'
)

add_dialogue('马总',
    '唉，说实话，干这么多年建筑，账一直稀里糊涂的。以前找代账做的，'
    '去年换了一家，感觉也没好哪去。我就想，你能不能帮我把财务规范起来？'
    '税该交的交，但别多交。再一个……今年接了俩大活儿，甲方要求挺严的，'
    '我怕年底查账出问题。'
)

add_mental_note(
    '五层消解漏斗——第一层·语言陷阱检测：\n'
    '  "规范起来"→ 具体指啥？账能看懂了？申报不错了？甲方查账拿得出手？\n'
    '  "别多交"→ 合法的税务筹划，还是想少交点？\n'
    '第二层·假设错误检测：\n'
    '  "代账没做好"→ 假设：代账是问题根源。但可能是业务端本身就乱，代账只是做不出来。\n'
    '第三层·逻辑错误检测：\n'
    '  "换了代账也没好"→ 换代账和账的质量改善是因果还是相关？如果业务端没变，换100个代账也没用。\n'
    '第四层·事实前提核查：\n'
    '  "接了俩大活儿"→ 多大？合同额多少？\n'
    '  "怕查账"→ 以前被查过？还是听说的？\n'
    '第五层·信息充分性：信息还不够回答"怎么规范"——缺前年代账报表、去年申报表、资金流状况。'
)

add_mental_note(
    '问题说明书五字段（当前状态）：\n'
    '  对象：建筑公司的财务体系\n'
    '  目标：改进（从代账模式转向顾问模式）\n'
    '  冲突：代账没达到预期，甲方要求变严\n'
    '  约束：未知（成本、人员、业务节奏都没说）→ 待追问\n'
    '  反馈：未知（"规范"和"查账没问题"的判定标准）→ 待追问'
)

add_dialogue('小阳',
    '马总您说这个我太理解了——代账公司做建筑行业的账确实容易出问题，'
    '因为建筑业的收入确认、成本归集跟普通商贸完全两码事。'
    '您说的"规范起来"，我多问一句——您对"规范"的预期是啥样？'
    '是把以前的账理清楚、心里有个底？还是从今年开始按新口径做，'
    '以后甲方查账能直接拿得出来？'
)

add_mental_note('用了卡内基·好感六法：共情（"我太理解了"）+ 提建设性选项（不是泛泛追问）')

add_dialogue('马总',
    '都有吧。以前那些账，代账做的我心里也没底，你帮我看看有没有坑。'
    '最主要的是以后——今年下半年有个500万的政府采购项目，'
    '甲方要求提供三年审计报告和完税证明。我怕现在这账拿不出手。'
)

add_mental_note(
    '消解漏斗第四层触发：\n'
    '  "500万的政府采购项目"——这个是实锤信息，有价值！\n'
    '问题说明书更新：\n'
    '  冲突明确了：甲方要求三年审计报告+完税证明，但现有代账账目支撑不了\n'
    '  目标清晰了：不是"规范"这个抽象概念，而是"应付甲方尽调+出具可审计的报表"'
)

add_dialogue('小阳',
    '明白了。那咱们分两步走：第一，我先把您去年和前年的账拉出来做个体检，'
    '看看代账做的底子怎么样、有没有需要补的坑；'
    '第二，从今年开始按审计标准做账，确保年底甲方查账时拿得出手。'
    '您觉得这个顺序行不行？'
)

add_dialogue('马总', '行，就是这个意思。')

add_separator()

# ── 第2步 ──

add_heading_styled('三、第二步：听老板说生意', level=1)

add_dialogue('小阳', '那咱们聊聊生意。公司主要做哪块业务？')

add_dialogue('马总',
    '主要做市政工程和房建，以前房建占大头，这几年市政越来越多了。'
    '去年总收入大概3000万，房建1800万，市政1200万。'
    '市政毛利比房建高，但是回款慢，甲方都是政府单位，流程走半年。'
)

add_mental_note(
    '捕捉关键数据：\n'
    '  - 双业务线，市政毛利高但回款慢\n'
    '  - 3,000万，刚好卡在小微企业边缘（人数？资产？需核实）\n'
    '  - 回款慢 = 资金压力大，可能涉及挂靠或转包'
)

add_dialogue('小阳', '回款慢确实头疼。主要客户是直接跟政府签，还是走总包分包？')

add_dialogue('马总',
    '都有。市政的直接跟区政府签，房建的基本都是分包——中建、中交下面的活。'
    '分包有个麻烦，就是甲方扣质保金、压进度款，有时候拖一年。'
)

add_mental_note(
    '消解漏斗继续跑：\n'
    '  - 分包 → 有没有资质挂靠的问题？\n'
    '  - 质保金压一年 → 其他应收款/其他应付款大概率有长期挂账\n'
    '  - 业务结构变化（房建→市政）→ 成本结构、发票类型都会变，代账可能没跟上'
)

add_dialogue('小阳', '资质这块呢？公司自己的资质够用，还是也要挂靠别人的？')

add_dialogue('马总', '我们自己有市政二级、房建三级，大部分够用。偶尔接大的也会挂别人，但不是常态。')

add_mental_note('判断：有证但偶尔挂靠——不是主要风险点，但备案时会关注。')

add_separator()

# ── 第3步 ──

add_heading_styled('四、第三步：摸底现状', level=1)

add_dialogue('小阳', '现在钱谁管、账谁做、税谁报？')

add_dialogue('马总',
    '我媳妇管钱，代账公司做账报税。每个月我把票拍给代账，'
    '他们出报表，我媳妇也看不懂，就放着。税都是代账直接报了，'
    '报之前会跟我说一声交多少。'
)

add_mental_note(
    '关键信号：\n'
    '  - 资金流离散（老婆管，但看不懂报表）\n'
    '  - 代账全权报税 → 可能存在申报数据与实际业务脱节\n'
    '  - 核心问题：老板不掌握自己的财务数据'
)

add_dialogue('小阳', '员工怎么发工资？有合同吗？')

add_dialogue('马总',
    '项目部的人基本都是老乡带出来的，没签合同，现金发。'
    '办公室几个人有合同，走银行。工地上的人最多的时候七八十人，'
    '少的时候二三十个，流动性大。'
)

add_mental_note(
    '触发核心公式·说服客户：不能上来就砸"你们用工违法"，要用话术引导。\n'
    '现用公式：避争→尊观点→友善→引导说是→让主意归他→共情'
)

add_dialogue('小阳',
    '工地流动性大，按天算工钱在建筑行业确实普遍——'
    '我之前服务的市政公司跟您情况差不多。'
    '不过您那个政府采购项目，如果甲方要求查社保和个税，现在这个情况能过吗？'
)

add_dialogue('马总', '……过不了。所以我才着急。')

add_mental_note('✅ 引导成功！他自己说出了痛点，不是我砸上去的。')

add_dialogue('小阳',
    '没事，咱们一步步来。我回头出一个分阶段的方案——'
    '先把甲方能查出来的雷排掉，再慢慢规范用工。'
    '不是一下子全改，您有3-6个月的过渡期。'
)

add_separator()

# ── 第4步 ──

add_heading_styled('五、第四步：收尾确认', level=1)

add_dialogue('小阳',
    '今天信息量不小，我总结一下我听到的几个重点方向：\n'
    '1. 今年有政府采购项目，需要审计报告和完税证明——这个是第一优先级\n'
    '2. 以前的代账账目先做个体检，看看遗留风险\n'
    '3. 用工和个税问题，咱们出个分阶段过渡方案\n'
    '4. 日常的账、税、票从我开始接手\n\n'
    '您看哪个最着急，我下周三之前先出一个方案。'
)

add_dialogue('马总', '政府采购那个最急，10月份要投标，现在7月了。你先帮我把去年的账理一理，看能不能出一份能见人的报表。')

add_dialogue('小阳',
    '好，那我下周三带两份东西过来：\n'
    '第一是去年的财务体检报告\n'
    '第二是政府采购项目的准备工作清单\n\n'
    '您需要提前把去年的合同、银行流水、代账给的报表都找出来，我到时候带电脑过来现场过。'
)

add_dialogue('马总', '行，我让人准备。')
add_dialogue('小阳', '好嘞，那先这样，下周三见。')

add_separator()

# ═══════════════════════════════════════
# 复盘
# ═══════════════════════════════════════

add_heading_styled('六、内功运用复盘', level=1)

add_heading_styled('6.1 五层消解漏斗运用记录', level=2)

add_table(
    ['层次', '触发时刻', '检测结果', '后续动作'],
    [
        ['第一层\n语言陷阱', '马总说"我想规范起来"', '发现"规范"无定义\n"别多交"有歧义', '追问：规范是理清底子还是应付甲方？\n→ 锁定了政府采购这个真实冲突'],
        ['第二层\n假设错误', '马总说"代账没做好"', '假设代账是根因，但可\n能业务端本身就乱', '不质疑，记在心里\n→ 后续摸底时核实业务端情况'],
        ['第三层\n逻辑错误', '马总说"换了代账也没好"', '把换代账和账的质量改善\n当成了因果', '不出声指出\n→ 出方案时用证据说话'],
        ['第四层\n事实前提', '马总说"接了俩大活儿"\n"怕查账"', '"500万政府采购"是实锤\n"怕查"来源未明确', '追问后锁定10月投标节点\n→ 明确第一优先级'],
        ['第五层\n信息充分性', '全程', '缺：报表、申报表、\n资金流、人员成本数据', '收尾时要求提前准备：\n合同+流水+代账报表'],
    ]
)

add_heading_styled('6.2 问题说明书填表过程', level=2)

add_table(
    ['字段', '初始状态', '对话后状态'],
    [
        ['对象', '建筑公司的财务体系', '锁定：前年代账账目 + 今年按审计标准做'],
        ['目标', '改进（模糊）', '明确：满足政府采购三年审计报告+完税证明要求'],
        ['冲突', '代账没达到预期', '具体化：甲方要求可审计报表，现有代账数据支撑不了'],
        ['约束', '未知', '部分明确：需分阶段过渡，不能影响业务节奏'],
        ['反馈', '未知', '部分明确：甲方能通过尽调+报表能见人'],
    ]
)

add_heading_styled('6.3 核心公式调用记录', level=2)

add_table(
    ['场景', '使用的核心公式', '具体话术'],
    [
        ['马总表达顾虑时\n（"账一直稀里糊涂"）', '卡内基·好感六法\n共情 → 提建设性选项', '"我太理解了——代账做建筑业的账\n确实容易出问题……您说的规范\n是理清底子还是以后能拿得出手？"'],
        ['发现用工问题时\n（现金发工资、没合同）', '说服客户·避争→引导说是\n→ 让主意归他', '"工地流动性大在建筑行业确实普遍\n……不过政府采购项目，\n甲方查社保个税能过吗？"'],
        ['马总承认"过不了"时\n（焦虑情绪出现）', '冯唐·九字真言\n不着急', '"没事，咱们一步步来。\n不是一下子全改，\n您有3-6个月的过渡期。"'],
    ]
)

add_heading_styled('6.4 五步出方案法·第零步半：交付场景判断', level=2)

add_body('客户状态判定：正常经营（年度顾问合同已签，非注销场景）')
add_body('交付范围：全面交付')

add_table(
    ['交付项', '本次是否执行', '理由'],
    [
        ['收入三表核对', '✅ 第一优先级', '政府采购需要可审计报表'],
        ['进销项发票核对', '✅ 随体检报告', '代账申报数据需验证'],
        ['银行对账', '✅ 随体检报告', '确认资金流与账载一致'],
        ['往来账龄分析', '✅ 关注质保金', '分包项目有长期质保金挂账'],
        ['工资个税核查', '✅ 分阶段', '先评估风险敞口，再出过渡方案'],
        ['存货/毛利率分析', '✅ 随体检报告', '市政vs房建毛利率差异需关注'],
        ['固定资产折旧测试', '✅ 常规', '建筑业设备较多'],
        ['费用限额速算', '✅ 常规', '招待费/广宣费等'],
    ]
)

add_heading_styled('6.5 三级校验分级执行', level=2)

add_body('本次座谈属于日常谈单场景，按P1级执行：')
add_body('Hermes（小阳）直接出对话 → 拿不准的判断（如用工风险表述方式）内部过了一道核验 → 确认后再回复。')
add_body('正式方案（体检报告+政府采购清单）将按P0级执行：双Agent交叉审核后方可交付。')

doc.add_page_break()

# ═══════════════════════════════════════
# 附录
# ═══════════════════════════════════════

add_heading_styled('附录：本轮进化注入一览', level=1)

add_body('本次模拟座谈为 xiaoyang-fusion v5.0（从 v4.1 升级）的首次综合实战演示。六项融合内功均在此次对话中被实际调用。')

add_table(
    ['序号', '来源 Skill', '注入模式', '注入位置', '本次调用次数'],
    [
        ['1', 'dbs-diagnosis', '五层消解漏斗', '沟通原则', '5层全部触发'],
        ['2', 'delivery-quality-check', '三级校验+数字铁律', '双Agent审核', 'P1级执行'],
        ['3', 'dbs-good-question', '问题说明书五字段', '第1步对齐期望', '全程追踪'],
        ['4', 'carnegie-influence', '场景索引+核心公式', '经典调用链', '3次调用'],
        ['5', 'caishui-report-generator', '实战陷阱速查', '交付行为规范', '代账数据陷阱激活'],
        ['6', 'messy-account-cleanup', '双场景交付区分', '五步出方案法', '确认正常经营->全面交付'],
    ]
)

# ── 保存 ──

output_path = r'D:\Desktop\模拟座谈_建筑公司马总.docx'
doc.save(output_path)
print(f'文档已保存：{output_path}')
