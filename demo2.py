from DrissionPage import ChromiumPage
import csv


#定义爬虫函数
def crawl_boss_api():
    #将操作模块实例化
    dp = ChromiumPage()
    base_url = 'https://www.zhipin.com/web/geek/job?query=Python爬虫&city=100010000'

    #创建csv文件
    with open('boss_jobs8.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f) #创建一个csv的编辑器
        writer.writerow([#写入列表字段
            '岗位名称','公司','薪资','学历'
            ,'经验','技能','城市','地区'
        ])
        #进行循环
        for page in range(35, 40):
            print(f'>>> 第 {page} 页')

            # 每页重新监听
            dp.listen.clear()
            dp.listen.start('wapi/zpgeek/search/joblist.json')

            # 每页重新 get（Boss 翻页的本质）
            dp.get(f'{base_url}&page={page}')
            dp.wait.load_start()

            resp = dp.listen.wait(timeout=15)
            if not resp:
                print('未捕获到接口')
                break

            job_list = resp.response.body.get('zpData', {}).get('jobList', [])
            if not job_list:
                print('本页无数据')
                break

            for job in job_list:
                writer.writerow([
                    job.get('jobName'),
                    job.get('brandName'),
                    job.get('salaryDesc'),
                    job.get('jobDegree'),
                    job.get('jobExperience'),
                    ','.join(job.get('skills') or []),
                    job.get('cityName'),
                    job.get('areaDistrict'),
                ])

    print('✅ 完成')

crawl_boss_api()