__author__ = 'Prathamesh.Tajane'

import re
import time
import urllib
import sys
from bs4 import BeautifulSoup
from time import gmtime, strftime

common_prifix = "https://en.wikipedia.org"
current_time = strftime("%Y-%m-%d-%H%M%S")

'''
 dfs(seed, keyword) Function

 description : dfs crawling of the urls as inOrder traversal
 Input:
    seed: The Url with depth in dict format
    keyword: The keyword to filter the crawled urls
 Output: Generate file with dfs crawled urls
'''


def dfs(seed, keyword):
    visited = []
    stack = [{'url': seed, 'depth': 1}]                 # add seed url in stack list alognwith its depth

    print('----------DFS Crawling started with keyword: {}----------'.format(str(keyword)))
    while (len(stack)!=0 and len(visited) < 1000):      # while condition to stopped crawling
        node = stack.pop()                              # select topmost dict of stack list
        if node['url'] not in (obj['url'] for obj in visited):  # to check if url is not already visited
            visited.append(node)                        # mark node as visited by appending it to visited list
            with open('dfs_' + str(keyword) + '_' + current_time + '.txt', 'a') as myfile:  # append node in file
                myfile.write(common_prifix + node['url'] + '\n')
            if (node['depth'] < 5):                     # condition to crawl only till depth : 5
                urls = findurl(node, keyword)           # find all url in given node (from top to bottom of the page)
                if len(urls)!=0:                        #add crawledUrl list to stack list only if available
                    crawledUrl = urls[::-1]             # reverse the url so first url is always on top of stack (from bottom to top of the page)
                    stack = stack + crawledUrl          # add crawled urls list to stack list
    print('----------The number of pages crawled are {}----------'.format(len(visited)))


'''
 bfs(seed, keyword) Function

 description : bfs crawling of the urls
 Input:
    seed: The Url with depth in dict format
    keyword: The keyword to filter the crawled urls
 Output: Generate file with bfs crawled urls
'''


def bfs(seed, keyword):
    visited = []
    queue = [{'url': seed, 'depth': 1}]                 # add seed url in stack list alognwith its depth

    print('----------BFS Crawling started with keyword: {}----------'.format(str(keyword)))
    while (len(queue)!=0 and len(visited) < 1000):      # while condition to stopped crawling
        node = queue.pop(0)                             # select first dict of stack list
        if node['url'] not in (obj['url'] for obj in visited):  # to check if url is not already visited
            visited.append(node)                        # mark node as visited by appending it to visited list
            with open('bfs_' + str(keyword) + '_' + current_time + '.txt', 'a') as myfile:  # append node in file
                myfile.write(common_prifix + node['url'] + '\n')
            if (node['depth'] < 5):                     # condition to crawl only till depth : 5
                urls = findurl(node, keyword)           # find all url in given node (from top to bottom of the page)
                if len(urls)!=0:                        #add crawledUrl list to stack list only if available
                    queue = queue + urls                # add crawled urls list to stack list
    print('----------The number of pages crawled are {}----------'.format(len(visited)))

'''
 findurl(node, keyword) Function

 description : Function to crawl the node with given keyword (focus crawling)
 Input:
    node: The Url with depth in dict format
    keyword:The keyword to filter the crawled urls
 Output: Example is[{'url':'/wiki/Sustainable1', depth: '2' }, {'url':'/wiki/Sustainable2', depth: '2' }, etc]

 Example:
 Input:
    node: {'url':'/wiki/Sustainable_energy', depth: '1' }
    keyword:(optional) 'solar
 Output: [{'url':'/wiki/Sustainable1', depth: '2' }, {'url':'/wiki/Sustainable2', depth: '2' }, etc]
'''


def findurl(node, keyword):
    try:
        #time.sleep(1)                               # be polite and use a delay of at least 1 sec
        htmltext = urllib.urlopen(common_prifix + node['url']).read()   # get and read the file from webpage
        soup = BeautifulSoup(htmltext, "html.parser")
        output = []
        for link in soup.findAll('a', href=True):   # find all the links from seed page
            if re.search('#', link['href']):        # ignore url that contains '#' (properly treat URLs with #)
                continue
            if re.search(':', link['href']):        # ignore url that contains ':' (avoid administrative link)
                continue
            if link['href'].startswith('/Main_Page') :
                continue
            if keyword is not None:
                if link['href'].startswith('/wiki') and re.search(keyword, link['href'],re.IGNORECASE):  # contains 'keyword'
                    output.append({'url': link['href'], 'depth': node['depth'] + 1})    #append urls to output list
            if keyword is None:
                if link['href'].startswith('/Main_Page'):
                    continue
                if link['href'].startswith('/wiki'):  # contains 'keyword'
                    output.append({'url': link['href'], 'depth': node['depth'] + 1})    #append urls to output list
        return output
    except IOError as err:
        print("No network route to the host".format(err))


def main():
    '''
     Input: python filename <seed> <bfs/dfs> <keyword>
     Then: sys.argv = [filename, <seed>, <bfs/dfs>, <keyword>]

     Answers:
         1. python crawler.py /wiki/Sustainable_energy bfs
         2a. python crawler.py /wiki/Sustainable_energy bfs solar
         2b. python crawler.py /wiki/Sustainable_energy dfs solar
         3. python crawler.py /wiki/Solar_power bfs
    '''
    if len(sys.argv) > 3:
        keyword = sys.argv[3]
    elif len(sys.argv) < 3:
        sys.exit('Format to run: python {0} <seed> <bfs/dfs> <key>(optional)'.format(sys.argv[0]))
    else:
        keyword = None
    seed = sys.argv[1]
    if sys.argv[2] == 'bfs':
        bfs(seed, keyword)  # call to bfs function
    if sys.argv[2] == 'dfs':
        dfs(seed, keyword)  # call to dfs function


if __name__ == '__main__':
    main()
