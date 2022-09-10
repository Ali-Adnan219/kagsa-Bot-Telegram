import os,platform,subprocess,base64,sys,re,requests,json,random,time,datetime

import re



def errors (theErr,get_value_back=False, lineno=None):
    # Get Error Text & Type
    ErrStr=str(theErr).replace('<string>','<file>').replace('.',' . ').replace('expected an indented block after function definition' , 'empty code block')
    ErrType=theErr.__class__.__name__.replace('error','ERR').replace('Error','ERR').replace('compiler.classes.__init__.','').replace('.',' . ')

    if lineno!=None:
        lll = re.findall(r'line \d+',ErrStr)
        for i in lll: ErrStr=ErrStr.replace(i , 'line '+lineno)
    # Start Decoding Texts
    #
    ###########################################################################
    text=ErrStr.replace('(','').replace(')','').replace('"','').replace('\'','')
    text=text.replace('__','_C')
    for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNMأبتثج'):
        text=text.replace(c,'C')
    COUNT=-1
    for i in text.split(' '):
        COUNT+=1
        i=i[1:]
        i=i.replace('_C','')
        if i =='':
            ORG=ErrStr.split(' ')[COUNT]
            Org=ErrStr.split(' ')[COUNT].replace('__','ة').replace('_','').replace('ة','_')
            ErrStr=ErrStr.replace(ORG,Org)
    #
    ###########################################################################
    text=ErrType.replace('(','').replace(')','').replace('"','').replace('\'','')
    text=text.replace('__','_C')
    for c in list('1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNMأبتثج'):
        text=text.replace(c,'C')
    COUNT=-1
    for i in text.split(' '):
        COUNT+=1
        i=i[1:]
        i=i.replace('_C','')
        if i =='':
            ORG=ErrType.split(' ')[COUNT]
            Org=ErrType.split(' ')[COUNT].replace('__','ة').replace('_','').replace('ة','_')
            ErrType=ErrType.replace(ORG,Org)
    ###########################################################################
    #
    # Somethings..
    Symbols = {
        'أ' : '@',
        'ب' : '$',
        'ت' : '^',
        'ث' : '~',
        'ج' : '?'
    }
    for i in Symbols.items():
        ErrStr = ErrStr.replace(i[0], i[1])
        ErrType = ErrType.replace(i[0], i[1])
    ErrType=ErrType.replace(' . ','.')
    ErrStr=ErrStr.replace(' . ','.').replace('STR_SYM_TWO','\\"').replace("STR_SYM_ONE","\\'").replace("STR_SYM_THREE","\\``")
    # Return a Values or Print it
    if get_value_back:
        return [ErrType, ErrStr, f'{ErrType} : {ErrStr}']
    else:
        print(f'{ErrType} : {ErrStr}',end='')


def t_o_I_n_t (value):
    try:    return int(value)
    except: raise ValueError(f'can\'t change ({value}) to int')
def t_o_S_t_r (value):
    try :  return str(value)
    except: raise ValueError(f'can\'t change ({value}) to str')
def t_o_F_l_o_a_t (value):
    try:  return float(value)
    except: raise ValueError(f'can\'t change ({value}) to float')
def i_s_I_n_t (value):
    if value.__class__.__name__ == 'int':
        return 1
    else:
        return 0
def i_s_S_t_r (value):
    if value.__class__.__name__ == 'str':
        return 1
    else:
        return 0
def i_s_F_l_o_a_t (value):
    if value.__class__.__name__ == 'float':
        return 1
    else:
        return 0

def i_s_L_i_s_t (value):
    if value.__class__.__name__ == 'list':
        return 1
    else:
        return 0

def i_s_D_i_c_t (value):
    if value.__class__.__name__ == 'dict':
        return 1
    else:
        return 0

def n_l_i_s_t (num, z_e_r_o=True):
    d = []
    if z_e_r_o:
        for i in range(0,num+1): d.append(i)
    else:
        for i in range(1,num+1): d.append(i)
    return d

n_l = '\n'
n_o_n_e = None
n_o_t = lambda co:not(co)

# Methods Starts from Here...
def r_e_p_l_a_c_e (DATA,v1,v2):
    if 'str' in DATA.__class__.__name__:
        return DATA.replace(v1,v2)
    else:
        raise ValueError('"replace()" function take only (str) value')
def s_p_l_i_t (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.split(value)
    else:
        raise ValueError('"split()" function take only (str) value')
def e_n_d (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.endswith(value)
    else:
        raise ValueError('"end()" function take only (str) value')
def s_t_a_r_t (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.startswith(value)
    else:
        raise ValueError('"start()" function take only (str) value')
def s_e_a_r_c_h (DATA,value):
    if ('str' in DATA.__class__.__name__):
        return DATA.find(value)
    else:
        raise ValueError('"search()" function take only (str) value')
def u_p_c_a_s_e (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.upper()
    else:
        raise ValueError('"upcase()" function take only (str) value')
def d_o_w_n_c_a_s_e (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.lower()
    else:
        raise ValueError('"downcase()" function take only (str) value')
def s_t_r_i_p (DATA):
    if ('str' in DATA.__class__.__name__):
        return DATA.strip()
    else:
        raise ValueError('"delspace()" function take only (str) value')



# List Function
def l_i_s_t (*arg):
    d = []
    for i in arg: d.append(i)
    return d
# LIST, DICT, STR
def l_e_n_g_t_h (DATA):
    if ('dict' in DATA.__class__.__name__) or ('list' in DATA.__class__.__name__) or ('str' in DATA.__class__.__name__):
        return len(DATA)
    else:
        raise ValueError('"length(DATA)" function take only (dict, list, str) value')
# LIST, DICT, STR
def g_e_t (DATA,*value):
    if (('list' in DATA.__class__.__name__)) or (('dict' in DATA.__class__.__name__)) or ('str' in DATA.__class__.__name__) :
        if len(value)>1:
            if 'dict' in DATA.__class__.__name__: raise ValueError('"get(VAR , value)" function take only (list, str) value')
            return DATA[value[0]:value[1]]
        else:
            return DATA[value[0]]
    else:
        raise ValueError('"get(VAR , *value)" function take only (dict, list, str) value')
# LIST, DICT
def a_p_p_e_n_d (DATA,*arguments):
    if 'list' in DATA.__class__.__name__:
        for i in arguments :
            DATA.append(i)
    elif 'dict' in DATA.__class__.__name__:
        DATA[arguments[0]]=arguments[1]
    else:
        raise ValueError('"append(VAR , value)" function take only (list, dict) value')
# LIST, DICT
def c_l_e_a_r (DATA):
    if (('list' in DATA.__class__.__name__)) or (('dict' in DATA.__class__.__name__)):
        DATA.clear()
        return 1
    else:
        raise ValueError('"clear(VAR)" function take only (list, dict) value')
# LIST, DICT
def d_e_l_e_t_e (DATA,value,i_d_x=False):
    if ('list' in DATA.__class__.__name__):
        if i_d_x and (i_s_I_n_t(value)):
            DATA.pop(value)
        elif i_d_x==False:
            DATA.remove(value)
        else:
            raise ValueError('"dalete(VAR, value, idx=BOOL)" if "idx" = true -> value must be int')
    elif (('dict' in DATA.__class__.__name__)):
        DATA.pop(value)
    else:
        raise ValueError('"delete(VAR , value, idx=BOOL)" function take only (list, dict) value')
    return 1
# LIST, DICT
def a_d_d (DATA,pos,value):
    if (('list' in DATA.__class__.__name__)):
        if not(i_s_I_n_t(pos)):
            raise ValueError('"add(VAR, pos, val)" pos must be int')
        DATA.insert(pos,value)
    elif (('dict' in DATA.__class__.__name__)):
        DATA[pos]=value
    else:
        raise ValueError('"add()" function take only (list, dict) value')
    return 1
# LIST
def i_n_d_e_x (DATA,value):
    if (('list' in DATA.__class__.__name__)):
        return DATA.index(value)
    else:
        raise ValueError('"index(VAR , value)" function take only (list) value')
# LIST
def a_p_p_l_i_s_t (DATA,value):
    if ('list' in DATA.__class__.__name__) and ('list' in value.__class__.__name__):
        DATA.extend(value)
    else:
        raise ValueError('"applist(VAR , value)" function take only (list) values')
    return 1
# LIST, STR
def c_o_u_n_t (DATA,value):
    if (('list' in DATA.__class__.__name__)) or (('str' in DATA.__class__.__name__)):
        return DATA.count(value)
    else:
        raise ValueError('"count(VAR , value)" function take only (list) value')
# LIST
def j_o_i_n (DATA,value):
    if (('list' in DATA.__class__.__name__)):
        return value.join(DATA)
    else:
        raise ValueError('"join(VAR , value)" function take only (list) value')



# Dict Function
def d_i_c_t (**arg):
    dct={}
    for i in arg:
        text=i.replace('__','$').replace('_','').replace('$','_')
        dct[text]=arg[i]
    return dct
# DICT
def k_e_y_s (DATA):
    if (('dict' in DATA.__class__.__name__)):
        return DATA.keys()
    else:
       raise ValueError('"keys(VAR)" function take only (dict) values')
# DICT
def v_a_l_u_e_s (DATA):
    if (('dict' in DATA.__class__.__name__)):
        return DATA.values()
    else:
        raise ValueError('"values(VAR)" function take only (dict) values')



def A_s_s_e_r_t_i_o_n_E_R_R (text):
    raise AssertionError(text)
def A_t_t_r_i_b_u_t_e_E_R_R (text):
    raise AttributeError(text)
def E_O_F_E_R_R (text):
    raise EOFError(text)
def F_l_o_a_t_i_n_g_P_o_i_n_t_E_R_R (text):
    raise FloatingPointError(text)
def G_e_n_e_r_a_t_o_r_E_x_i_t (text):
    raise GeneratorExit(text)
def I_m_p_o_r_t_E_R_R (text):
    raise ImportError(text)
def I_n_d_e_x_E_R_R (text):
    raise IndexError(text)
def K_e_y_E_R_R (text):
    raise KeyError(text)
def K_e_y_b_o_a_r_d_I_n_t_e_r_r_u_p_t (text):
    raise KeyboardInterrupt(text)
def M_e_m_o_r_y_E_R_R (text):
    raise MemoryError(text)
def N_a_m_e_E_R_R (text):
    raise NameError(text)
def N_o_t_I_m_p_l_e_m_e_n_t_e_d_E_R_R (text):
    raise NotImplementedError(text)
def O_S_E_R_R (text):
    raise OSError(text)
def O_v_e_r_f_l_o_w_E_R_R (text):
    raise OverflowError(text)
def R_e_f_e_r_e_n_c_e_E_R_R (text):
    raise ReferenceError(text)
def R_u_n_t_i_m_e_E_R_R (text):
    raise RuntimeError(text)
def S_t_o_p_I_t_e_r_a_t_i_o_n (text):
    raise StopIteration(text)
def S_y_n_t_a_x_E_R_R (text):
    raise SyntaxError(text)
def I_n_d_e_n_t_a_t_i_o_n_E_R_R (text):
    raise IndentationError(text)
def T_a_b_E_R_R (text):
    raise TabError(text)
def S_y_s_t_e_m_E_R_R (text):
    raise SystemError(text)
def S_y_s_t_e_m_E_x_i_t (text):
    raise SystemExit(text)
def T_y_p_e_E_R_R (text):
    raise TypeError(text)
def U_n_b_o_u_n_d_L_o_c_a_l_E_R_R (text):
    raise UnboundLocalError(text)
def U_n_i_c_o_d_e_E_R_R (text):
    raise UnicodeError(text)
def U_n_i_c_o_d_e_E_n_c_o_d_e_E_R_R (text):
    raise UnicodeEncodeError(text)
def U_n_i_c_o_d_e_D_e_c_o_d_e_E_R_R (text):
    raise UnicodeDecodeError(text)
def U_n_i_c_o_d_e_T_r_a_n_s_l_a_t_e_E_R_R (text):
    raise UnicodeTranslateError(text)
def V_a_l_u_e_E_R_R (text):
    raise ValueError(text)
def Z_e_r_o_D_i_v_i_s_i_o_n_E_R_R (text):
    raise ZeroDivisionError(text)
def N_e_w_E_R_R (name):
    ss={}
    exec(f'class {name} (Exception):\n\tpass\ndef rrr (text):\n\traise {name}(text)',ss)
    return ss['rrr']
class ParseError (Exception):pass

def parse_id (value,parseMemory):
    # Catch Error
    if 'else :' in parseMemory[5]: # else can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to else command')
    if 'except Exception as ERROR :' in parseMemory[5]: # catch can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to catch command')
    if 'try :' in parseMemory[5]: # try can't take ID after
        raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nCan\'t add any arguments to try command')
    
    # Replace All The Symbols in The Var Name : @$^~:?
    value = value.replace('@','أ').replace('$','ب').replace('^','ت').replace('~','ث').replace('?','ج')
    
    # Variables that more than 1 Length :
    # my_name   or   my_age
    if (len(value)>2) or (len(value)==2 and not(value.startswith('#'))):
        # Replace From This         To This
        # my_var                    m_y___v_a_r
        value='_'.join(list(value))
    
    # 4h5  =  ID
    # #4  =  ID
    if value[0] in '1234567890' :
        value='_'+value
    
    # catch the words that used in class
    if (value == 'أ_c_o_n_s_t_r_u_c_t_o_r')    : value='__init__' 
    if (value == 'أ_s_t_r_i_n_g')    : value='__str__' 
    if (value == 'أ_r_e_p_r')    : value='__repr__' 
    if (value == 'أ_t_h_i_s')    : value='self' 

    # if function name not set yet
    if '|DATA_N|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA_N|',value)
    # if |DATA-P| not set yet
    elif '|DATA-P|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA-P|',value)
    # if |DATA| in line
    elif '|DATA|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA|',f'{value}|DATA|')
    # if var name not set yet
    elif '|DATA0|' in parseMemory[5]:
        parseMemory[5]=parseMemory[5].replace('|DATA0|',value+'|DATA0|')
    # if this is var & is named
    elif '|DATA1|' in parseMemory[5]:
        if not(' = ' in parseMemory[5]): # if not named ( = in line (var ii (=) data))
            parseMemory[5]=parseMemory[5].replace('|DATA1|',f'{value}|DATA1|')
        else:
            raise SyntaxError(f'invalid syntax (<file>, line {parseMemory[4]})\nVariable opened without assign')
        # line is empty
    elif parseMemory[5]=='':
        parseMemory[5]+=f'{value}|DATA|'
    else:
        raise ParseError(f'can\'t parsing (<file>, line {parseMemory[4]})')

    return parseMemory
#


class K_e_y_b_o_a_r_d:
    class KeyboardError (Exception) :pass
    def w_a_i_t (text):
        try:
            keyboard.wait(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    def w_r_i_t_e (text):
        try:
            keyboard.write(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    def n_e_w_H_o_t_k_e_y (text, func):
        try:
            keyboard.add_hotkey(text, func)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
    class r_e_c_o_r_d:
        def __init__ (self,u_n_t_i_l=''):
            try:
                self.record = keyboard.record(until= u_n_t_i_l)
                self.g_e_t = []
                for i in self.record:
                    self.g_e_t.append(str(i).replace('KeyboardEvent(','')[0:-1])
            except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))
        def p_l_a_y_A_l_l (self,s_p_e_e_d=0.5):
            keyboard.play(self.record, speed_factor = s_p_e_e_d)
    def p_r_e_s_s (text):
        try:
            keyboard.press_and_release(text)
        except Exception as ee : raise K_e_y_b_o_a_r_d.KeyboardError(str(ee))


class M_a_t_h:
    def a_c_o_s (*arg) :
        return math.acos(*arg)
    def a_c_o_s_h (*arg) :
        return math.acosh(*arg)
    def a_s_i_n (*arg) :
        return math.asin(*arg)
    def a_s_i_n_h (*arg) :
        return math.asinh(*arg)
    def a_t_a_n (*arg) :
        return math.atan(*arg)
    def a_t_a_n_2 (*arg) :
        return math.atan2(*arg)
    def a_t_a_n_h (*arg) :
        return math.atanh(*arg)
    def c_e_i_l (*arg) :
        return math.ceil(*arg)
    def c_o_m_b (*arg) :
        return math.comb(*arg)
    def c_o_p_y_s_i_g_n (*arg) :
        return math.copysign(*arg)
    def c_o_s (*arg) :
        return math.cos(*arg)
    def c_o_s_h (*arg) :
        return math.cosh(*arg)
    def d_e_g_r_e_e_s (*arg) :
        return math.degrees(*arg)
    def d_i_s_t (*arg) :
        return math.dist(*arg)
    def e (*arg) :
        return math.e(*arg)
    def e_r_f (*arg) :
        return math.erf(*arg)
    def e_r_f_c (*arg) :
        return math.erfc(*arg)
    def e_x_p (*arg) :
        return math.exp(*arg)
    def e_x_p_m_1 (*arg) :
        return math.expm1(*arg)
    def f_a_b_s (*arg) :
        return math.fabs(*arg)
    def f_a_c_t_o_r_i_a_l (*arg) :
        return math.factorial(*arg)
    def f_l_o_o_r (*arg) :
        return math.floor(*arg)
    def f_m_o_d (*arg) :
        return math.fmod(*arg)
    def f_r_e_x_p (*arg) :
        return math.frexp(*arg)
    def f_s_u_m (*arg) :
        return math.fsum(*arg)
    def g_a_m_m_a (*arg) :
        return math.gamma(*arg)
    def g_c_d (*arg) :
        return math.gcd(*arg)
    def h_y_p_o_t (*arg) :
        return math.hypot(*arg)
    def i_n_f (*arg) :
        return math.inf(*arg)
    def i_s_c_l_o_s_e (*arg) :
        return math.isclose(*arg)
    def i_s_f_i_n_i_t_e (*arg) :
        return math.isfinite(*arg)
    def i_s_i_n_f (*arg) :
        return math.isinf(*arg)
    def i_s_n_a_n (*arg) :
        return math.isnan(*arg)
    def i_s_q_r_t (*arg) :
        return math.isqrt(*arg)
    def l_c_m (*arg) :
        return math.lcm(*arg)
    def l_d_e_x_p (*arg) :
        return math.ldexp(*arg)
    def l_g_a_m_m_a (*arg) :
        return math.lgamma(*arg)
    def l_o_g (*arg) :
        return math.log(*arg)
    def l_o_g_1_0 (*arg) :
        return math.log10(*arg)
    def l_o_g_1_p (*arg) :
        return math.log1p(*arg)
    def l_o_g_2 (*arg) :
        return math.log2(*arg)
    def m_o_d_f (*arg) :
        return math.modf(*arg)
    def n_a_n (*arg) :
        return math.nan(*arg)
    def n_e_x_t_a_f_t_e_r (*arg) :
        return math.nextafter(*arg)
    def p_e_r_m (*arg) :
        return math.perm(*arg)
    def p_i (*arg) :
        return math.pi(*arg)
    def p_o_w (*arg) :
        return math.pow(*arg)
    def p_r_o_d (*arg) :
        return math.prod(*arg)
    def r_a_d_i_a_n_s (*arg) :
        return math.radians(*arg)
    def r_e_m_a_i_n_d_e_r (*arg) :
        return math.remainder(*arg)
    def s_i_n (*arg) :
        return math.sin(*arg)
    def s_i_n_h (*arg) :
        return math.sinh(*arg)
    def s_q_r_t (*arg) :
        return math.sqrt(*arg)
    def t_a_n (*arg) :
        return math.tan(*arg)
    def t_a_n_h (*arg) :
        return math.tanh(*arg)
    def t_a_u (*arg) :
        return math.tau(*arg)
    def t_r_u_n_c (*arg) :
        return math.trunc(*arg)
    def u_l_p (*arg) :
        return math.ulp(*arg)


class R_a_n_d_o_m:
    def s_t_r (length, a_b_c=True, c_a_p=True, n_u_m=True, a_d_d=''):
        chars = ''
        if a_b_c:
            chars+='qwertyuioplkjhgfdsazxcvbnm'
            if c_a_p:
                chars+='QWERTYUIOPLKJHGFDSAZXCVBNM'
        if n_u_m:
            chars+='0123456789'
        chars+=a_d_d
        chars = chars * 2
        return ''.join(random.sample(chars,length))
    def i_n_t (s,e):
        return random.randint(s,e)
    def o_n_e_O_f (data):
        return random.choice(data)


class C_o_d_e:
    class CodeError (Exception):
        pass
    class u_t_f___8 :
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'bytes':
                raise C_o_d_e.CodeError('utf-8 input data must be bytes')
            return data.decode('utf-8')
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('utf-8 input data must be string')
            return data.encode('utf-8')
    class b_a_s_e_6_4 :
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('base64 input data must be string')
            base64_byte = data.encode('ascii')
            ascii_data = base64.b64decode(base64_byte)
            return ascii_data.decode('ascii')
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('base64 input data must be string')
            encoded_ascii = data.encode('ascii')
            base64_byte = base64.b64encode(encoded_ascii)
            return base64_byte.decode('ascii')
    class h_e_x :
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('hex input data must be string')
            data=data.encode('utf-8')
            data2 = data.hex()
            return data2
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('hex input data must be string')
            data2 = bytes.fromhex(data)
            data2 = data2.decode('ascii')
            return data2
    class b_i_n_a_r_y :
        def e_n_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('binary input data must be string')
            return "".join(format(ord(i),'08b')for i in data)
        def d_e_c_o_d_e (data):
            if data.__class__.__name__ != 'str':
                raise C_o_d_e.CodeError('binary input data must be string')
            out=''
            d2=list(data)
            end=[]
            while len(d2)!=0:
                end.append(''.join(d2[0:8]))
                d2=d2[8:]
            for value in end:
                an_integer = int(value,2)
                ascii_char = chr(an_integer)
                out+=ascii_char
            return out


class J_S_O_N:
    class JsonError (Exception):
        pass
    class p_a_r_s_e :
        def __init__(self,data):
            if data.__class__.__name__ == 'str' :
                data = J_S_O_N.t_o_D_i_c_t( data )
            if data.__class__.__name__ == 'dict' :
                pass
            else:
                raise J_S_O_N.JsonError('JSON.pasre() take only str/dict value')

            for i in data.keys():
                if data[i].__class__.__name__ == 'dict':
                    try :     exec(f'self.{"_".join(list(i))} = J_S_O_N.p_a_r_s_e({data[i]})')
                    except:  raise J_S_O_N.JsonError(f'value error : "{i}"')
                else:
                    if data[i].__class__.__name__ == 'str':
                        data[i] = f'"{data[i]}"'
                    try :     exec(f'self.{"_".join(list(i))} = {data[i]}')
                    except:  raise J_S_O_N.JsonError(f'value error : "{i}"')
    def u_n_P_a_r_s_e (data):
        if not('p_a_r_s_e' in data.__class__.__name__):
            raise J_S_O_N.JsonError('JSON.unPasre() take only "JSON.parse()" value')
        outdict = {}
        for i in dir(data):
            if len(re.findall(r'__[a-zA-Z0-9_]*__',i)) > 0 :
                continue
            i2 = i.replace('__','ة').replace('_','').replace('ة','_')
            exec(f'''if J_S_O_N.p_a_r_s_e == data.{i}.__class__:\n\toutdict["{i2}"] = J_S_O_N.u_n_P_a_r_s_e(data.{i})\nelse:\n\texec(f'outdict["{i2}"] = data.{i}')''')
        return outdict
    def t_o_J_s_o_n (data):
        try:
            return json.dumps(data)
        except Exception as e:
            raise J_S_O_N.JsonError(str(e))
    def t_o_D_i_c_t (data):
        try:
            return json.loads(data)
        except Exception as e:
            raise J_S_O_N.JsonError(str(e))


class H_T_T_P:
    def __init__ (self):
        self.session=requests.Session()
        self.url=''
        self.method=''
    class HTTPRequestError (Exception):
        'For Any Request Error'
        pass
    class response:
        def __init__ (self,data):
            self.u_r_l            =  data.url
            self.r_e_d_i_r_e_c_t  =  data.is_redirect
            self.c_o_o_k_i_e_s    =  data.cookies.get_dict()
            self.h_e_a_d_e_r_s    =  data.headers
            self.t_e_x_t          =  data.text
            self.c_o_n_t_e_n_t    =  data.content
            self.c_o_d_e          =  data.status_code
    def h_e_a_d_e_r_s (self,data):
        self.session.headers.update(data)
    def e_n_c_o_d_i_n_g (self,data):
        self.session.encoding = data
    def a_u_t_h (self,data):
        self.session.auth=data
    def c_o_o_k_i_e_s (self,data):
        self.session.cookies.update(data)
    def U_R_L (self,*url):
        if len(url) < 1 :
            raise self.HTTPRequestError('Enter a Url in "HTTP().URL( URL_HERE )" function')
        self.url='/'.join(url)
    def m_e_t_h_o_d (self,data):
        if data.upper().strip() in ['GET','POST','PUT','DELETE','HEAD','PATCH','OPTIONS']:
            self.method=data.upper().strip()
        else:
            raise self.HTTPRequestError('Unknown Method You Can Use (GET, POST)')
    def s_e_n_d (self,*data):
        try:
            if self.method=='': raise self.HTTPRequestError('Please Set HTTP Request Method "HTTP().method( METHOD_HERE )"')
            if self.url=='':    raise self.HTTPRequestError('Please Set Request URL "HTTP().url( URL_HERE )"')
            
            if self.method == 'GET':
                if len(data) >= 1 :   req=self.session.get(self.url, data=data[0])
                else:                 req=self.session.get(self.url)
            if self.method == 'POST':
                if len(data) >= 1 :   req=self.session.post(self.url, data=data[0])
                else:                 req=self.session.post(self.url)
            if self.method == 'PUT':
                if len(data) >= 1 :   req=self.session.put(self.url, data=data[0])
                else:                 req=self.session.put(self.url)
            if self.method == 'DELETE':
                if len(data) >= 1 :   req=self.session.delete(self.url, data=data[0])
                else:                 req=self.session.delete(self.url)
            if self.method == 'HEAD':
                if len(data) >= 1 :   req=self.session.head(self.url, data=data[0])
                else:                 req=self.session.head(self.url)
            if self.method == 'PATCH':
                if len(data) >= 1 :   req=self.session.patch(self.url, data=data[0])
                else:                 req=self.session.patch(self.url)
            if self.method == 'OPTIONS':
                if len(data) >= 1 :   req=self.session.options(self.url, data=data[0])
                else:                 req=self.session.options(self.url)
            
            return self.response(req)
        except Exception as e:
            raise self.HTTPRequestError(str(e))


class R_e_g_e_x :
    def __init__ (self,reStr):
        self.re_str=fr'{reStr}'
    def i_s_M_a_t_c_h (self,string):
        if re.search(self.re_str,string):
            return True
        else:
            return False
    def f_i_n_d_A_l_l (self,string):
        return re.findall(self.re_str,string)
    def i_n_d_e_x_S_t_a_r_t (self,string):
        try:
            return re.search(self.re_str,string).start()
        except:
            return -1
    def i_n_d_e_x_E_n_d (self,string):
        try:
            return re.search(self.re_str,string).end()
        except:
            return -1
    def s_p_l_i_t (self,string,t_i_l_l=None):
        if t_i_l_l==None:
            return re.split(self.re_str,string)
        else:
            return re.split(self.re_str,string,t_i_l_l)
    def r_e_p_l_a_c_e(self,string,join):
        return re.sub(self.re_str, join, string)
    

class S_y_s_t_e_m:
    a_r_g_v = sys.argv[1:]
    def i_n_p_u_t():
        return sys.stdin.readline()
    class w_r_i_t_e :
        def o_u_t (*text):
            for i in text : sys.stdout.write(i)
            return 1
        def e_r_r (*text):
            print(*text, file = sys.stderr)
            return 1
    def e_x_i_t (text):
        sys.exit(text)
    def c_m_d (command):
        os.system(command)
        return 0
    def e_x_e_c (command,s_h_e_l_l=True):
        DEVNULL = subprocess.DEVNULL
        try:
            return subprocess.check_output(command,shell=s_h_e_l_l, stderr = DEVNULL , stdin = DEVNULL ).decode("utf-8",errors='backslashreplace')
        except Exception as e:
            class execError (Exception): pass
            raise execError(str(e))
            '''def execErrors(er):
                raise execError(str(er))
            ss={'execErrors':execErrors}
            exec(f'ret = lambda: execErrors("{str(e)}")',ss)
            return ss['ret']'''
    def p_a_t_h ():
        return os.getcwd()
    def i_n_f_o_r_m_a_t_i_o_n_s ():
        UNAME = platform.uname()
        out = {
            'system':UNAME.system,
            'node':UNAME.node,
            'release':UNAME.release,
            'version':UNAME.version,
            'machine':UNAME.machine,
            'processor':UNAME.processor,
        }
        return out


class F_i_l_e:
    class R_e_a_d:
        def __init__ (self,filename):
            self.F = open (filename,'r')
        def g_e_t_T_e_x_t (self):
            return self.F.read()
        def e_n_d (self):
            self.F.close()
    class ReadBytes:
        def __init__ (self,filename):
            self.g_e_t = open(filename,'rb').read()
    class W_r_i_t_e:
        def __init__ (self,filename):
            self.F = open(filename,'w')
        def w_r_i_t_e (self,*arguments):
            for arg in arguments:
                self.F.write(arg)
        def e_n_d (self):
            self.F.close()
    class A_d_d:
        def __init__ (self,filename):
            self.F = open(filename,'a')
        def w_r_i_t_e (self,*arguments):
            for arg in arguments:
                self.F.write(arg)
        def e_n_d (self):
            self.F.close()


class T_i_m_e:
    class get_time_data :
        def __init__ (self,obj):
            self.y_e_a_r  = obj.tm_year
            self.m_o_n  = obj.tm_mon
            self.m_d_a_y  = obj.tm_mday
            self.h_o_u_r  = obj.tm_hour
            self.m_i_n  = obj.tm_min
            self.s_e_c  = obj.tm_sec
            self.w_d_a_y  = obj.tm_wday
            self.y_d_a_y  = obj.tm_yday
            self.i_s_d_s_t  = obj.tm_isdst
    def e_p_o_c_h () :
        return time.time()
    def a_E_p_o_c_h (num, o_b_j = False) :
        if o_b_j:
            return T_i_m_e.get_time_data( time.localtime(num) )
        else:
            return time.ctime(num)
    def s_l_e_e_p (num) :
        time.sleep(num)
    def n_o_w (o_b_j = False) :
        if o_b_j:
            return T_i_m_e.get_time_data( time.localtime( time.time() ) )
        else:
            return time.ctime( time.time() )
    class c_o_u_n_t:
        def __init__ (self,o_b_j=False):
            pass
            self.obj = o_b_j
            self.time = 0
        def s_t_a_r_t (self):
            self.time =  datetime.datetime.now()
        def e_n_d (self):
            if self.obj:
                obj = datetime.datetime.now() - self.time
                self.d_a_y_s = obj.days
                self.m_i_n = obj.min
                self.s_e_c_o_n_d_s = obj.seconds
                self.m_i_c_r_o_s_e_c_o_n_d_s = obj.microseconds
                self.t_o_t_a_l___s_e_c_o_n_d_s = obj.total_seconds()
            else:
                self.g_e_t = str(datetime.datetime.now() - self.time)