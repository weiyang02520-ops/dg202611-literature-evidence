# -*- coding: utf-8 -*-
"""BDS SMS patch: append official docs + standards to raw pool and matrix (2026-08-30)."""
import io
import csv

BASE = r'C:\Users\peng\Desktop\zcode\DG-202611_literature_research'

pool_rows = [
"BDS-11,北斗卫星导航系统应用服务体系（1.0版）（BDS-ASA-1.0）,中国卫星导航系统管理办公室,2019,中国卫星导航系统管理办公室（官方文件，2019-12-27 发布）,,,http://www.beidou.gov.cn/yw/xwzx/202001/t20200110_19921.html,BeiDou SMS,""official service architecture; RSMC; GSMC; service frequency; short message"",REAL,【BDS-ASA-PATCH 新增 OFFICIAL-01】官方服务体系文件：表5 RSMC 公开服务频度（一般1次/30秒、最高1次/1秒）、服务成功率、响应时延、终端发射功率、服务容量、最大报文长度；表6 GSMC 公开服务成功率、响应时延、最大报文长度——直接证伪旧库'发送频次限制无官方公开数值'结论。,VERIFIED,\"发布主体与日期经北斗官网解读页（http://www.beidou.gov.cn/yw/xwzx/202001/t20200110_19921.html，2020-01-10，含封面照：中国卫星导航系统管理办公室 二〇一九年十二月）核验；官网解读确认'区域短报文系统容量提升10倍、用户功率降至3W'；表5/表6数值经权威镜像全文转载与政府分站（最高频度1秒1次、传输时延约0.5秒、容量1000万次/小时）交叉一致。\",3,YES,官方文件。频度核心值（一般1次/30秒、最高1次/1秒）双通道一致；表值细项（成功率≥95%、时延≤1s/≤1分钟、容量1000万次/小时）建议后续以官方原件复核后引用。",
"BDS-12,新时代的中国北斗（白皮书）,中华人民共和国国务院新闻办公室,2022,国务院新闻办公室（白皮书，2022-11-04 发布）,,,https://www.gov.cn/zhengce/2022-11/04/content_5724658.htm,BeiDou SMS,""white paper; regional short message; global short message; service scope"",REAL,【BDS-ASA-PATCH 新增 OFFICIAL-02】官方白皮书：区域短报文通信服务单次通信能力从120汉字提升至1000汉字（14000比特）、可发送图片；全球短报文通信服务单次通信能力40汉字（560比特）；服务范围（区域：中国及周边地区；全球：全球范围）。与 BDS-01 发布会口径一致。,VERIFIED,\"gov.cn 官方白皮书全文（https://www.gov.cn/zhengce/2022-11/04/content_5724658.htm）经 web_reader 核验标题与短报文规格要点；14000比特/1000汉字、560比特/40汉字与 BDS-01 官网发布会口径一致。\",1,YES,官方文件。服务范围表述以白皮书原文为准（区域短报文服务范围为中国及周边地区）。",
"BDS-STD-01,GB/T 44087-2024 北斗三号区域短报文通信用户终端技术要求与测试方法,国家市场监督管理总局；国家标准化管理委员会,2024,推荐性国家标准（GB/T）,,,https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=4E47A9DC691D8386E23E70B070241B0E,BeiDou SMS,""national standard; BDS-3 regional short message; user terminal; technical requirements; test methods"",REAL,【BDS-ASA-PATCH 新增】现行国标：DG 短报文终端选型与测试方法的对标依据（终端技术要求与测试方法）。,VERIFIED,\"国家标准全文公开系统（openstd.samr.gov.cn）详情页核验：标准状态=现行；发布日期=2024-05-28；实施日期=2024-05-28；主管部门/归口部门=中央军委装备发展部；发布单位=国家市场监督管理总局、国家标准化管理委员会；CCS=M30；ICS=33.060.01；英文标准名称=Technical requirements and test methods for BDS-3 regional short message communication user terminal。另经北斗官网《北斗已发布国家标准及专项标准清单》（2024-07-18）与《发布...等6项北斗国家标准》（2024-06-03，2024年第9号公告）双核验。\",0,YES,标准元数据全部核验；标准文本内容未取得（公开系统在线预览受限），引用限于标准号/名称/状态/日期/归口层级。",
"BDS-STD-02,GB/T 44086.1-2024 北斗三号区域短报文通信用户终端信息接口 第1部分：用户管理模块接口,国家市场监督管理总局；国家标准化管理委员会,2024,推荐性国家标准（GB/T）,,,https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=506087828A7A2CD16CBEACA713794DDD,BeiDou SMS,""national standard; user terminal information interface; user management module"",REAL,【BDS-ASA-PATCH 新增】现行国标：DG 短报文终端接入的用户管理模块接口对标依据。,VERIFIED,\"国家标准全文公开系统详情页核验：现行；发布/实施日期=2024-05-28；主管部门/归口部门=中央军委装备发展部；发布单位=国家市场监督管理总局、国家标准化管理委员会；CCS=M30；ICS=33.060.01；英文标准名称=Information interface for BDS-3 regional short message communication user terminal—Part 1: User management module interface。北斗官网标准清单双核验（清单第42项）。\",0,YES,标准元数据全部核验；文本内容未取得，引用限于元数据层级。",
"BDS-STD-03,GB/T 44086.2-2024 北斗三号区域短报文通信用户终端信息接口 第2部分：通用数据接口,国家市场监督管理总局；国家标准化管理委员会,2024,推荐性国家标准（GB/T）,,,https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=7B4912068CF2F627212B6F63B8648592,BeiDou SMS,""national standard; user terminal information interface; general data interface"",REAL,【BDS-ASA-PATCH 新增】现行国标：DG 短报文终端通用数据接口（遥测报文编码对接）对标依据。,VERIFIED,\"国家标准全文公开系统详情页核验：现行；发布/实施日期=2024-05-28；主管部门/归口部门=中央军委装备发展部；发布单位=国家市场监督管理总局、国家标准化管理委员会；CCS=M30；ICS=33.060.01；英文标准名称=Information interface for BDS-3 regional short message communication user terminal—Part 2: General data interface。北斗官网标准清单双核验（清单第43项）。\",0,YES,标准元数据全部核验；文本内容未取得，引用限于元数据层级。",
]

with io.open(BASE + r'\01_RAW_LITERATURE_POOL.csv', 'r', encoding='utf-8-sig') as f:
    c = f.read()
if not c.endswith('\n'):
    c += '\n'
c += '\n'.join(pool_rows) + '\n'
with io.open(BASE + r'\01_RAW_LITERATURE_POOL.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(c)

matrix_rows = [
"PM-200,BDS-11,BeiDou SMS,2019,区域短报文通信服务（RSMC，中国及周边地区）；官方体系文件表5；系统服务指标口径,REAL,,,,服务频度（service frequency）,,一般 1次/30秒；最高 1次/1秒,次/秒,UNSPECIFIED,UNSPECIFIED,,,OFFICIAL-DOC,表5 区域短报文通信服务：服务频度 一般1次/30秒、最高1次/1秒（北斗官网解读+权威镜像/政府分站交叉一致）,,【边界】官方系统服务指标，非 DG 终端实测；实际可用频度受服务权限/终端能力/场景影响，以实测为准【BDS-ASA-PATCH】。不得与 GSMC 混写,NO,官方文件数值；终端实测前仅作设计约束引用,YES",
"PM-201,BDS-11,BeiDou SMS,2019,区域短报文通信服务（RSMC）表5 其余服务指标；系统服务指标口径,REAL,,,,服务成功率/响应时延/终端发射功率/服务容量/最大报文长度,,≥95%（成功率）；≤1s（时延）；≤3W量级（功率）；约1000万次/小时（容量）；14000 bit=1000汉字（报文）,%/s/W/次每小时/bit,UNSPECIFIED,UNSPECIFIED,,,OFFICIAL-DOC,表5：服务成功率≥95%、响应时延≤1s、终端发射功率≤3W量级、服务容量约1000万次/小时、最大报文长度14000比特（官网解读页'容量提升10倍、用户功率降至3W'交叉印证）,,【边界】系统指标口径；成功率/时延为官方承诺值非项目实测【BDS-ASA-PATCH】,NO,官方文件数值；细项建议以官方原件复核,YES",
"PM-202,BDS-11,BeiDou SMS,2019,全球短报文通信服务（GSMC，全球范围）表6；系统服务指标口径,REAL,,,,服务成功率/响应时延/最大报文长度,,≥95%（成功率）；≤1分钟（时延）；560 bit=40汉字（报文）,%/分钟/bit,UNSPECIFIED,UNSPECIFIED,,,OFFICIAL-DOC,表6 全球短报文通信服务：服务成功率≥95%、响应时延≤1分钟、最大报文长度560比特（与 BDS-01/白皮书 560比特/40汉字口径一致）,,【边界】GSMC 参数不得与 RSMC（14000比特/1s时延）混写；系统指标非项目实测【BDS-ASA-PATCH】,NO,官方文件数值；细项建议以官方原件复核,YES",
]

with io.open(BASE + r'\03_PERFORMANCE_BENCHMARK_MATRIX.csv', 'r', encoding='utf-8-sig') as f:
    m = f.read()
if not m.endswith('\n'):
    m += '\n'
m += '\n'.join(matrix_rows) + '\n'
with io.open(BASE + r'\03_PERFORMANCE_BENCHMARK_MATRIX.csv', 'w', encoding='utf-8', newline='') as f:
    f.write(m)

for path, ncols, label in [(BASE + r'\01_RAW_LITERATURE_POOL.csv', 17, 'pool'), (BASE + r'\03_PERFORMANCE_BENCHMARK_MATRIX.csv', 24, 'matrix')]:
    with io.open(path, encoding='utf-8') as f:
        parsed = list(csv.reader(f))
    bad = [(i, len(r), r[0][:12] if r else '?') for i, r in enumerate(parsed) if len(r) != ncols]
    print(label, 'rows:', len(parsed), 'bad:', bad[:5])
