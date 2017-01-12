
    #############################################################
    #                                                           #
    #   This program is relased in the GNU GPL v3.0 licence     #
    #   you can modify/use this program as you wish. Please     #
    #   link the original distribution of this software. If     #
    #   you plan to redistribute your modified/copied copy      #
    #   you need to relased the in GNU GPL v3.0 licence too     #
    #   according to the overmentioned licence.                 #
    #                                                           #
    #   "PROUDLY" MADE BY chkrr00k (i'm not THAT proud tbh)     #
    #                                                           #
    #############################################################
    #                                                           #
    #                                                           #
    #                            YEE                            #
    #                                                           #
    #                                                           #
    #############################################################

import urllib.request
import re
import http.client


PATTERN_HTTP_WWW = "(http|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"
PATTERN_WWW = "([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"

class HTTPRequest:
    def __init__(self, url):
        uncomplete = self.__isUncompleteUrl(url)
        if not self.__isCompleteUrl(url) and not uncomplete:
            raise Exception("Invalid Url")
        if uncomplete:
            url = self.__completeUrl(url)
        self.__url = url
        
    def __isCompleteUrl(self, string):
        return re.search(PATTERN_HTTP_WWW, string) is not None

    def __isUncompleteUrl(self, string):
        return re.search(PATTERN_WWW, string) is not None

    def __completeUrl(self, string):
        return "https://" + string

    def __disassembleUrl(self, string):
        s = re.search(PATTERN_HTTP_WWW, string)
        group = s.groups()
        return group[1], group[2]

    def __get(self, address, location, method):
        conn = http.client.HTTPConnection(address)
        conn.request(method=method, url=location)
        p = conn.getresponse()
        return p.getheaders()

    def __processHeader(self, headerList):
        headerMap = dict()
        for tup in headerList:
            headerMap[tup[0]] = tup[1]
        return headerMap

    def getHeader(self):
        add, loc = self.__disassembleUrl(self.__url)
        if add.startswith("www."):
            add = add[4:]
        heads = self.__get(add, loc, 'HEAD')
        return self.__processHeader(heads)

    def get(self, method):
        add, loc = self.__disassembleUrl(self.__url)
        if add.startswith("www."):
            add = add[4:]
        return self.__get(add, loc, method)
