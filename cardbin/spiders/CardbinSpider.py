import scrapy

from cardbin.items import CardbinItem


class CardbinSpider(scrapy.Spider):
    name = 'cardbin'  # 爬虫名称，与运行命令一致
    allowed_domains = ['bincheck.org']  # 限制域名，避免爬取无关网站
    """启动请求：发送列表页请求，回调指定为列表页解析方法"""
    start_url = [# 'https://bincheck.org/costa-rica',
        # 'https://bincheck.org/cambodia',
        # 'https://bincheck.org/turkey',
        # 'https://bincheck.org/chad',
        # 'https://bincheck.org/cyprus',
        # 'https://bincheck.org/samoa',
        # 'https://bincheck.org/cayman-islands',
        # 'https://bincheck.org/slovenia',
        # 'https://bincheck.org/vietnam',
        #          'https://bincheck.org/kuwait',
        # 'https://bincheck.org/jamaica',
        #          'https://bincheck.org/antigua-and-barbuda',
        # 'https://bincheck.org/cameroon',
        #          'https://bincheck.org/saudi-arabia',
        # 'https://bincheck.org/cape-verde',
        #          'https://bincheck.org/bosnia-and-herzegovina',
        # 'https://bincheck.org/guinea-bissau',
        #          'https://bincheck.org/netherlands',
        # 'https://bincheck.org/gambia',
        # 'https://bincheck.org/nigeria',
        #          'https://bincheck.org/lebanon',
        # 'https://bincheck.org/cook-islands',
        # 'https://bincheck.org/bahamas',
        #          'https://bincheck.org/australia',
        # 'https://bincheck.org/uganda',
        # 'https://bincheck.org/slovakia',
        #          'https://bincheck.org/argentina',
        # 'https://bincheck.org/turks-and-caicos-islands',
        #          'https://bincheck.org/belize',
        # 'https://bincheck.org/mongolia',
        # 'https://bincheck.org/senegal',
        #          'https://bincheck.org/hungary',
        # 'https://bincheck.org/san-marino',
        # 'https://bincheck.org/mozambique',
        #          'https://bincheck.org/uzbekistan',
        # 'https://bincheck.org/burundi',
        # 'https://bincheck.org/estonia',
        #          'https://bincheck.org/sri-lanka',
        # 'https://bincheck.org/puerto-rico',
        # 'https://bincheck.org/mexico',
        #          'https://bincheck.org/kosovo',
        # 'https://bincheck.org/peru',
        # 'https://bincheck.org/anguilla',
        #          'https://bincheck.org/bhutan',
        # 'https://bincheck.org/algeria',
        #          'https://bincheck.org/central-african-republic',
        # 'https://bincheck.org/kyrgyzstan',
        #          'https://bincheck.org/malaysia',
        # 'https://bincheck.org/spain',
        # 'https://bincheck.org/serbia',
        #          'https://bincheck.org/south-korea',
        # 'https://bincheck.org/jordan',
        # 'https://bincheck.org/belarus',
        #          'https://bincheck.org/niger',
        # 'https://bincheck.org/zimbabwe',
        # 'https://bincheck.org/ireland',
        #          'https://bincheck.org/djibouti',
        # 'https://bincheck.org/haiti',
        # 'https://bincheck.org/malawi',
        #          'https://bincheck.org/iceland',
        # 'https://bincheck.org/dominica',
        #          'https://bincheck.org/trinidad-and-tobago',
        # 'https://bincheck.org/austria',
        #          'https://bincheck.org/panama',
        # 'https://bincheck.org/south-africa',
        # 'https://bincheck.org/poland',
        #
        #          'https://bincheck.org/honduras',
        # 'https://bincheck.org/laos',
        # 'https://bincheck.org/luxembourg',
        #          'https://bincheck.org/comoros',
        # 'https://bincheck.org/albania',
        # 'https://bincheck.org/mauritania',
        'https://bincheck.org/montserrat', 'https://bincheck.org/andorra', 'https://bincheck.org/virgin-islands-us',
        'https://bincheck.org/thailand', 'https://bincheck.org/fiji', 'https://bincheck.org/guatemala',
        'https://bincheck.org/singapore', 'https://bincheck.org/seychelles', 'https://bincheck.org/nicaragua',
        # 'https://bincheck.org/united-states',
        'https://bincheck.org/turkmenistan', 'https://bincheck.org/venezuela',
        'https://bincheck.org/switzerland', 'https://bincheck.org/ukraine', 'https://bincheck.org/burkina-faso',
        'https://bincheck.org/syria', 'https://bincheck.org/tajikistan', 'https://bincheck.org/nepal',
        'https://bincheck.org/saint-vincent-and-the-grenadines', 'https://bincheck.org/yemen',
        'https://bincheck.org/norway', 'https://bincheck.org/tunisia', 'https://bincheck.org/germany',
        'https://bincheck.org/equatorial-guinea', 'https://bincheck.org/palestine', 'https://bincheck.org/suriname',
        'https://bincheck.org/israel', 'https://bincheck.org/rwanda', 'https://bincheck.org/british-virgin-islands',
        'https://bincheck.org/malta', 'https://bincheck.org/egypt', 'https://bincheck.org/maldives',
        'https://bincheck.org/botswana', 'https://bincheck.org/grenada', 'https://bincheck.org/guam',
        'https://bincheck.org/papua-new-guinea', 'https://bincheck.org/aruba', 'https://bincheck.org/sweden',
        'https://bincheck.org/namibia', 'https://bincheck.org/bolivia', 'https://bincheck.org/portugal',
        'https://bincheck.org/brazil', 'https://bincheck.org/lithuania', 'https://bincheck.org/macau',
        'https://bincheck.org/pakistan', 'https://bincheck.org/kazakhstan', 'https://bincheck.org/belgium',
        'https://bincheck.org/uruguay', 'https://bincheck.org/afghanistan', 'https://bincheck.org/liberia',
        'https://bincheck.org/chile', 'https://bincheck.org/iran', 'https://bincheck.org/bahrain',
        'https://bincheck.org/vanuatu', 'https://bincheck.org/georgia', 'https://bincheck.org/greece',
        'https://bincheck.org/croatia', 'https://bincheck.org/denmark', 'https://bincheck.org/united-kingdom',
        'https://bincheck.org/el-salvador', 'https://bincheck.org/italy', 'https://bincheck.org/benin',
        'https://bincheck.org/saint-lucia', 'https://bincheck.org/libya', 'https://bincheck.org/india',
        'https://bincheck.org/gibraltar', 'https://bincheck.org/united-arab-emirates', 'https://bincheck.org/tanzania',
        'https://bincheck.org/mauritius', 'https://bincheck.org/ecuador', 'https://bincheck.org/mali',
        'https://bincheck.org/swaziland', 'https://bincheck.org/ghana', 'https://bincheck.org/brunei-darussalam',
        'https://bincheck.org/france', 'https://bincheck.org/bangladesh', 'https://bincheck.org/liechtenstein',
        'https://bincheck.org/latvia', 'https://bincheck.org/tonga', 'https://bincheck.org/morocco',
        'https://bincheck.org/montenegro', 'https://bincheck.org/new-zealand', 'https://bincheck.org/oman',
        'https://bincheck.org/kenya', 'https://bincheck.org/iraq', 'https://bincheck.org/angola',
        'https://bincheck.org/hong-kong', 'https://bincheck.org/moldova', 'https://bincheck.org/guyana',
        'https://bincheck.org/colombia', 'https://bincheck.org/armenia', 'https://bincheck.org/canada',
        'https://bincheck.org/japan', 'https://bincheck.org/bermuda', 'https://bincheck.org/vatican-city',
        'https://bincheck.org/bulgaria', 'https://bincheck.org/taiwan-china', 'https://bincheck.org/indonesia',
        'https://bincheck.org/ethiopia', 'https://bincheck.org/madagascar', 'https://bincheck.org/china',
        'https://bincheck.org/dominican-republic', 'https://bincheck.org/sierra-leone', 'https://bincheck.org/qatar',
        'https://bincheck.org/guinea', 'https://bincheck.org/barbados', 'https://bincheck.org/czech-republic',
        'https://bincheck.org/paraguay', 'https://bincheck.org/russia', 'https://bincheck.org/zambia',
        'https://bincheck.org/philippines', 'https://bincheck.org/azerbaijan',
        'https://bincheck.org/saint-kitts-and-nevis', 'https://bincheck.org/gabon', 'https://bincheck.org/romania',
        'https://bincheck.org/togo', 'https://bincheck.org/finland']

    def start_requests(self):
        for url in self.start_url:
            self.logger.info(f"开始爬取列表页: {url}")
            yield scrapy.Request(url=url, meta={"playwright": True},  # 启用Playwright渲染
                callback=self.parse_page_list,  # 关键：回调到列表页解析方法
                # errback=self.handle_error  # 错误处理
            )

    async def parse_page_list(self, response):
        """解析列表页：提取详情页URL + 处理分页"""
        self.logger.info(f"正在解析列表页: {response.url}")

        # 1. 提取详情页链接（使用你代码中的选择器 "span.monts a::attr(href)"）
        detail_links = response.css("span.monts a::attr(href)").getall()

        # 去重（避免重复链接）
        detail_links = list(set(detail_links))

        if not detail_links:
            self.logger.warning(f"列表页 {response.url} 未找到详情页链接，请检查选择器是否正确")
        else:
            self.logger.debug(f"列表页 {response.url} 找到 {len(detail_links)} 个详情页链接")
            for link in detail_links:
                detail_url = response.urljoin(link)  # 补全相对URL为绝对URL
                yield scrapy.Request(url=detail_url, meta={"playwright": True}, callback=self.parse_detail_page,
                    # 关键：回调到详情页解析方法
                    errback=self.handle_error)

        # 2. 处理分页（关键：将分页逻辑移出循环，避免重复判断）
        next_page_li = response.css('li.next')
        # 检查下一页按钮是否被禁用（包含disabled类）
        if 'disabled' in next_page_li.attrib.get('class', ''):
            self.logger.info(f"{response.url} 是最后一页，无下一页")
            return

        # 提取下一页链接并发送请求
        next_page_href = next_page_li.css('a::attr(href)').get()
        if next_page_href:
            next_page_url = response.urljoin(next_page_href)
            self.logger.info(f"发现下一页列表: {next_page_url}")
            yield scrapy.Request(url=next_page_url, meta={"playwright": True}, callback=self.parse_page_list,
                # 下一页仍回调列表页解析方法
                # errback=self.handle_error
            )
        else:
            self.logger.warning(f"{response.url} 未找到下一页链接")

    async def parse_detail_page(self, response):
        """解析详情页：提取表格数据并生成Item"""
        self.logger.info(f"正在解析详情页: {response.url}")
        item = CardbinItem()

        # 1. 基础字段
        item['url'] = response.url  # 详情页URL

        # 2. 解析两个目标表格（根据你提供的HTML结构）
        tables = response.css('table.table.table-bordered.bin-table')
        self.logger.debug(f"详情页 {response.url} 找到 {len(tables)} 个目标表格")

        # 解析第一个表格（BIN卡基本信息）
        if len(tables) >= 1:
            first_table = tables[0]
            item['bin_iin'] = first_table.css('tr:contains("BIN/IIN") td::text').get(default='').strip()
            item['brand'] = (first_table.css('tr:contains("Brand") td a::text').get(default='') or first_table.css(
                'tr:contains("Brand") td::text').get(default='')).strip()
            item['card_type'] = first_table.css('tr:contains("Type") td::text').get(default='').strip()
            item['category'] = first_table.css('tr:contains("Category") td::text').get(default='').strip()

        # 解析第二个表格（银行及地理位置信息）
        if len(tables) >= 2:
            second_table = tables[1]
            item['bank'] = second_table.css('tr:contains("Bank") td::text').get(default='').strip()
            item['bank_url'] = second_table.css('tr:contains("Bank URL") td::text').get(default='').strip()
            item['country'] = (
                        second_table.css('tr:contains("Country") td a::text').get(default='') or second_table.css(
                    'tr:contains("Country") td::text').get(default='')).strip()
            item['country_short'] = second_table.css('tr:contains("Country Short") td::text').get(default='').strip()
            item['latitude'] = second_table.css('tr:contains("Latitude") td::text').get(default='').strip()
            item['longitude'] = second_table.css('tr:contains("Longitude") td::text').get(default='').strip()

        # 3. 生成Item（数据会自动进入SQLitePipeline存储）
        yield item

    def handle_error(self, failure):
        """错误处理：打印失败日志"""
        self.logger.error(f"请求失败: {failure.request.url}")
        self.logger.error(f"错误原因: {repr(failure.value)}")
