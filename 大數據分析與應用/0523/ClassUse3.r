# install necessary library
install.packages("xml2")
install.packages("dplyr")
install.packages("tidyverse")
install.packages("jsonlite")
install.packages("rvest")

# Load necessary libraries
library(xml2)
library(dplyr)
library(tidyverse)
library(rvest)

# Define the RSS feed URL (example RSS feed about Tesla Model Y)
rss_url <- "https://news.google.com/rss/search?q=Tesla+Model+Y&hl=en-US&gl=US&ceid=US:en"

# Read the RSS feed
rss_feed <- read_xml(rss_url)

# Parse the RSS feed
items <- rss_feed %>%
  xml_find_all("//item")

items[1]

#===============================================================================

# 提取連結
links <- items %>%
  xml_find_all(".//link") %>%
  xml_text()

links[1]


# 提取描述
descriptions <- items %>%
  xml_find_all(".//description") %>%
  xml_text()

descriptions[1]

# 移除 HTML 標籤的函數
remove_html_tags <- function(html_string) {
  # 解析 HTML 內容
  parsed_html <- read_html(html_string)
  # 提取文本內容
  text_content <- html_text(parsed_html)
  return(text_content)
}

# 將函數應用到所有描述中
clean_descriptions <- sapply(descriptions, remove_html_tags, USE.NAMES = FALSE)

clean_descriptions[1]

#===============================================================================

# 提取發佈日期
pub_dates <- items %>%
  xml_find_all(".//pubDate") %>%
  xml_text()

pub_dates[1]
# [1] "Wed, 22 May 2024 15:39:00 GMT"

# 創建包含提取信息的資料框
tesla_news <- data.frame(
  title = titles,
  link = links,
  description = clean_descriptions,
  pub_date = pub_dates,
  stringsAsFactors = FALSE
)

# 打印資料框的前幾行
print(head(tesla_news))

#===============================================================================

