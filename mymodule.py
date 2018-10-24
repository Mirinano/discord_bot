import os
import urllib.request

def split_function(content, start_line=1, argument=None, punctuation="=", * , split="\n", rest_return=True):
        return_dict = dict()
        content_list = content.split(split)
        if start_line >= 2:
            if rest_return:
                return_dict["rest_first"] = split.join(content_list[:(start_line - 1)])
            else:
                pass
            del content_list[:(start_line - 1)]
        else:
            pass
        if argument is None:
            num = 0
            for cl in content_list:
                if punctuation in cl:
                    cll = cl.split(punctuation)
                    return_dict[cll[0]] = punctuation.join(cll[1:])
                    num += 1
                else:
                    break
            del content_list[:num]
            if rest_return:
                return_dict["rest_last"] = split.join(content_list)
            else:
                pass
            return return_dict
        elif type(argument) is str:
            num = 1
            for cl in content_list:
                if argument in cl.split(punctuation):
                    return_dict[argument] = punctuation.join(cl.split(punctuation)[1:])
                    del content_list[:num]
                    break
                else:
                    num += 1
            if rest_return:
                return_dict["rest_last"] = split.join(content_list)
            else:
                pass
            return return_dict
        elif type(argument) in (list, set, tuple):
            num = 0
            num_else = 0
            for cl in content_list:
                cll = cl.split(punctuation)
                if cll[0] in argument:
                    return_dict[cll[0]] = punctuation.join(cll[1:])
                    num += 1
                    num += num_else
                    num_else = 0
                else:
                    num_else += 1
            del content_list[:num_else]
            if rest_return:
                return_dict["rest_last"] = split.join(content_list)
            else:
                pass
            return return_dict
        else:
            return dict()

def file_action(message):
        file_list = list()
        opener = urllib.request.build_opener()
        opener.addheaders=[("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0")]
        urllib.request.install_opener(opener)
        for sent_file in message.attachments:
            url = sent_file["proxy_url"]
            file_name = "./file_log/" + sent_file["filename"]
            if not os.path.exists(os.path.dirname(file_name)):
                os.makedirs(os.path.dirname(file_name))
            else:
                pass
            info = dict()
            if sent_file["size"] < 8*1024*1024:
                info["type"] = "file"
                info["file_name"] = file_name
                urllib.request.urlretrieve(url=url, filename=file_name) # save file if type is file.
            else:
                info["type"] = "url"
                info["url"] = url
            file_list.append(info)
        del sent_file
        del url
        del file_name
        del info
        return file_list
