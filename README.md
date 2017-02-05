# spider-web-crawler
Spider web crawler which can perform focused and unfocused web crawling with Depth First Search and Breadth 
first search Technique.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Web search engines and some other sites use Web crawling or spidering software to update their web content or 
indices of others sites' web content. Web crawlers can copy all the pages they visit for later processing by a 
search engine which indexes the downloaded pages so the users can search much more efficiently.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Instruction to execute this code :

Requirements: 

1. Python 2.7.x or more running on system (specifically 2.7.12) 
2. Required packages:  - urllib, sys, time, re, BeautifulSoup

Pre-requisites:

1. All the command takes certain time to execute because of politeness property of 1 second.
2. All the command will generate .txt files with at most 1000 entries in same working directory.

Command Execution:

1. Run the crawler.py using following command:
   python crawler.py <seed> <bfs/dfs> <key>(optional)

1.1  Unfoucused crawler: (with seed_url  /wiki/Sustainable_energy)
     cmd: python crawler.py /wiki/Sustainable_energy bfs
     output file: bfs_None_<currenttime>.txt

2.1 (a).Foucused Breath First Search crawler with keyword solar: (with seed_url /wiki/  Sustainable_energy) 
     cmd: python crawler.py /wiki/Sustainable_energy bfs solar
     output file: bfs_solar_<currenttime>.txt

2.1 b.Foucused DFS crawler with keyword solar: (with seed_url /wiki/Sustainable_energy) 
   cmd: python crawler.py /wiki/Sustainable_energy dfs solar
   output file: dfs_solar_<currenttime>.txt

3. Unfoucused crawler: (with seed_url /wiki/Solar_power)
   cmd: python crawler.py /wiki/Solar_power bfs
   output file: bfs_None_<currenttime>.txt

Note : For reference I have added the task name at the end of each .txt file 
which will not be observed while executing the crawler.py.All the .txt files will 
have same name as per the explanation given above.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Working of Web Crawler:

In breadth first crawling, the crawler starts crawling from given ‘seed URL’, and then scan each hyperlink on the seed URL’s webpage starting from the topmost URL (or hyperlink) which satisfy the criteria given in the problem statement, moving towards the bottom of the webpage. Once the crawler has crawled all the links on the ‘seed URL’ it marks it as ‘visited’ and increment the ‘depth counter’ to two as it has finished crawling the seed URL’s webpage. Now the crawler will move to the next webpage given by the first eligible hyperlink on seed URL’s webpage. It will again crawl all the hyperlinks on that webpage and mark it as ‘visited’, then it will move to the second URL which was obtained while crawling the seed URL’s webpage and will start crawling that webpage. Once all the URL’s are marked as visited, the ‘depth counter’ increments to three. This process of crawling the next URL’s will continue till the crawler visit 1000 unique URLs or it reaches depth 5. One thing should be noted that, in breadth first crawling the crawler visit all the URL’s that are at the same depth before moving to the URL’s which are at next depth level. That means the crawler moves horizontally from left to right. Thus this is known as ‘Breadth First Crawling’. During breadth first crawling we not only observed that it crawls the hot pages (webpages which are more important) first but also the average quality of crawled pages’ decreases as the crawler advances to the next depth level.

In depth first crawling, the crawler again starts with seed URL but instead of visiting webpages on the same depth like breath first crawler, it crawls the first URL of each visited page and move downwards unless it reaches depth 5 or visit 1000 unique URL’s. If it reaches depth 5 but has not visited 1000 unique URL’s then it continues to crawl the nearest ancestor with unvisited URL. Unlike the Breath first crawler, the depth first crawler craw deeper and deeper until all the pages on that path get crawled and then backtrack other branches of URL’s. In depth first crawling we can’t predict the order in which the webpages get crawled which might affect the ranking of webpages and search result quality.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

@author
Prathamesh Tajane
tajane.p@husky.neu.edu / ptajane@gmail.com
"Lets change the world,one line of code at a time."
