# dorks_hunter
简单的 Google Dorks 搜索工具

# 描述

这是一个小型实用工具，用于搜索硬编码的有用 Google Dorks

> 警告！这不是一个绕过 Google 的工具，如果你滥用这个工具，你将会收到 `HTTP Error 429: Too Many Requests` 的错误信息，这意味着你被禁止访问了 :) 如果出现这种情况，请在几个小时后再试一次。

# 安装

```bash
git clone https://github.com/XiaomingX/google_dork_attack
cd google_dork_attack
pip3 install -r requirements.txt
```

# 参数说明

- d (domain) - 目标域名
- r (results) - 返回结果数量
- o (output) - 输出文件

# 使用方法

```bash
> python3 dorks_hunter.py -h
usage: dorks_hunter.py [-h] --domain DOMAIN [--results RESULTS] [--output OUTPUT]

简单的 Google Dork 搜索工具

选项:
  -h, --help            显示帮助信息并退出
  --domain DOMAIN, -d DOMAIN
                        要扫描的目标域名
  --results RESULTS, -r RESULTS
                        每次搜索返回的结果数量，默认为 10
  --output OUTPUT, -o OUTPUT
                        输出文件
```                        

# 截图

## 默认搜索
![image](https://user-images.githubusercontent.com/24670991/182604961-26005889-a010-43db-a5f4-6faaf9ebeadc.png)

## 限制为 2 条结果并保存到输出文件
![image](https://user-images.githubusercontent.com/24670991/182605167-c518c162-3494-494f-91fe-65c94f130639.png)

## 输出文件的格式
![image](https://user-images.githubusercontent.com/24670991/182606542-a55aa2ab-38a0-405e-ac23-6c0d17b9f7ca.png)

