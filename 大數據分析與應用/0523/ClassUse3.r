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
# [1] "https://news.google.com/rss/articles/CBMiWWh0dHBzOi8vZWx1Y3RyZWsuY28vMjAyNC8wNS8yMi9gZWVwLWNvb"

# 提取描述
descriptions <- items %>%
  xml_find_all(".//description") %>%
  xml_text()

descriptions[1]
# [1] "<a href=\"https://news.google.com/rss/articles/CBMiWWh0dHBzOi8vZWx1Y3RyZWsuY28vMjAyNC8wNS8yMi9gZWVwLWNvb\">Jeep compares electric Wagoneer S to Tesla's Model Y in new teaser video</a>&nbsp;&nbsp;<font color=\""

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
# [1] "Jeep compares electric Wagoneer S to Tesla's Model Y in new teaser video Electrek.co"

