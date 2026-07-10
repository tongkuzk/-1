#一次爬虫实践学习，仅仅用于实践学习，不做任何商业用途
本次实践关键在于通过Drssionpage自动化，接管浏览器页面，通过浏览器的自动登录绕过普通爬虫的伪装过程，
直接进行页面登录，数据的爬取

#前期准备，需要先进行目标网址的登录，使用指令打开浏览器，再运行代码
1️. 彻底关闭所有 Edge
右键任务栏 → 任务管理器
结束所有 msedge.exe
2️. 打开 
按 Win + R→ 输入 cmd→ 回车
3. 复制下面整段命令，直接粘贴回车（不用改）：
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" ^
--remote-debugging-port=9222 ^
--user-data-dir="C:\Users\%USERNAME%\AppData\Local\Microsoft\Edge\User Data"
4. 运行代码即可
