# Local Excluded Sensitive Files

源目录中的排除项不会被修改或删除，只是不进入 GitHub 镜像。

| EXCLUDED_FILE | REASON | PDF_NOT_MIRRORED | SOURCE_URL | DOI | LOCAL_STATUS |
|---|---|---|---|---|---|
| `staging/xicp_tmp2.html` | 明显临时网页缓存（文件名含 `tmp`），不属于正式资产；包含一个邮箱地址，按隐私最小化与“无审计价值临时文件”规则排除 | NO | 未记录 | 未记录 | 保留在源目录，未修改 |

## 第三方全文

源目录没有 PDF 文件，因此没有第三方论文全文被镜像，也没有因 PDF 排除而删除或改变任何引用。

## 安全扫描说明

- 文件名规则扫描：未发现 `.env`、`*.pem`、`*.key`、SSH 私钥、credential、cookie、session、token、secret、password、浏览器 profile 等候选文件。
- 内容格式扫描：未发现常见 API key、GitHub token、OpenAI key、AWS access key、Bearer Authorization、密码赋值、Cookie/session、通用 secret 赋值、URL 内嵌凭据或私钥头。
- PII 格式扫描：未发现中国大陆手机号或身份证号；上述临时 HTML 命中一个邮箱地址并已排除。
- 本机未安装 `gitleaks`，因此没有运行该第三方扫描器；提交前另行执行同一规则集的镜像复扫和 Git 暂存差异检查。
