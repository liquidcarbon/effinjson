import json
import re
import sys

class fnClass:
    """
    example class for fj module
    will kick off a predefined function encoded in JSON as a string
    """
    def sum(json_arg_list):
        try:
            summed = sum(json_arg_list)
        except TypeError:
            summed = 'arguments must be numeric'
        except:
            summed = 'not sure what\'s going on here'
        return summed

    def cleanstring(json_arg_string):
        try:
            cleaned = re.sub('^\s+', '', json_arg_string)
            cleaned = re.sub('\s+$', '', cleaned)
            cleaned = re.sub('\s+', ' ', cleaned)
        except TypeError:
            cleaned = 'argument must be a string'
        except:
            cleaned = 'just what do you think you\'re doing?'
        return cleaned

    def divide(json_arg_list):
        try:
            assert len(json_arg_list) == 2
            divided = json_arg_list[0] / json_arg_list[1]
        except AssertionError:
            divided = 'wrong number of arguments'
        except TypeError:
            divided = 'arguments must be numeric'
        except: # ZeroDivisionError:
            divided = 'are you dividing by zero?'
        return divided

    def isprime(json_arg_number):
        """obviously recursive would be faster"""
        if type(json_arg_number) is not int:
            return None
        elif json_arg_number < 1:
            return None
        elif json_arg_number > 1e10:
            return 'too big'
        elif json_arg_number in [1,2]:
            return True
        else:
            for i in range(2, round(json_arg_number**0.5)):
                if json_arg_number % i == 0:
                    return False
        return True
#end fnClass

def effinJSON(JSON='test_json', fnclass=fnClass, print_results=False):
    #deserialization
    JSONError = json.JSONDecodeError
    with open(JSON,'r') as f:
        try:
            j = json.load(f)
        except JSONError as e:
            print('bad JSON: %s' % e)
            sys.exit(1)

    for k, v in j.items():
        if hasattr(fnClass, v['fn']):
            result = getattr(fnClass, v['fn'])(v['args'])
        else:
            result = 'function "%s" not defined' % v['fn']
        j[k]['result'] = result
        if print_results:
            print(v['fn'], '(', v['args'], ') = ', result, sep='')
    return j

if __name__=='__main__':
    try:
        r = effinJSON(JSON=sys.argv[1], print_results=True)
        print('\n', json.dumps(r, indent=4))
    except Exception as e:
        print(e, ', defaulting to test.json \n')
        effinJSON(JSON='test.json', print_results=True)
