import re,zipfile,os,sys,traceback
from __memory__ import *
def decodeString (string):
	data = ''
	for char in string: data += chr(ord(char)-2)
	return data
FullCodes = decodeString("%%%%%%%\"^pencuu\"iagavaGatataqat\"*+<^p\"\"\"\"fgh\"aakpkvaa\"*ugnh+\"<^p\"\"\"\"\"\"\"\"ugnh0vagazav\"\"\"\"\"?\"))^p\"\"\"\"\"\"\"\"ugnh0nakapagapaq\"?\"))^p\"\"\"\"\"\"\"\"ugnh0nakapag\"\"\"\"\"?\"))^p\"\"\"\"\"\"\"\"ugnh0va{arag\"\"\"\"\"?\"))^p\"\"\"\"\"\"\"\"ugnh0hakanag\"\"\"\"\"?\")ute1nkd0mi)^p\"\"\"\"\"\"\"\"vjgavd\"?\"vtcegdcem0gzvtcevavd*u{u0gzeakphq*+]4_+^p\"\"\"\"\"\"\"\"vdahkngpcog.\"vdankpgpq.\"vdahwpe.\"vdankpg\"?\"vjgavd]/3_^p\"\"\"\"\"\"\"\"vdahkngv{rg\"?\")r{)^p\"\"\"\"\"\"\"\"%\"rctug\"vjg\"gttqt\"hkngpcog^p\"\"\"\"\"\"\"\"%\"gttqt\"ecog\"htqo\"mciuc\"eqfg^p\"\"\"\"\"\"\"\"kh\"vdahkngpcog\"??\")>uvtkpi@)<^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0hakanag\"?\"mciucahkng^p\"\"\"\"\"\"\"\"\"\"\"\"vdahkngv{rg\"?\")mi)^p\"\"\"\"\"\"\"\"%\"hqto\"c\"nkdtct{^p\"\"\"\"\"\"\"\"gnkh\")mivor)\"kp\"vdahkngpcog<^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0hakanag\"?\"vdahkngpcog0urnkv*qu0ugr+]/3_0tgrnceg*)aockp0r{).))+^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0hakanag\"?\"ugnh0hakanag0tgrnceg*)aa).)ث)+0tgrnceg*)a).))+0tgrnceg*)ث).)a)+^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0hakanag-?\")0min)^p\"\"\"\"\"\"\"\"%\"uqogvjkpi\"gnug^p\"\"\"\"\"\"\"\"gnug<^p\"\"\"\"\"\"\"\"\"\"\"\"fcvcahqwpfgf\"?\"Hcnug^p\"\"\"\"\"\"\"\"\"\"\"\"hqt\"vvd\"kp\"vjgavd<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"vdahp.\"vdanpq.\"vdah.\"a\"?\"vvd^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"kh\"*vdahp\"??\")>uvtkpi@)+<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"vdahkngpcog.\"vdankpgpq.\"vdahwpe.\"a\"?\"vvd^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"fcvcahqwpfgf\"?Vtwg^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"dtgcm^p\"\"\"\"\"\"\"\"\"\"\"\"kh\"pqv*fcvcahqwpfgf+<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"vdankpgpq\"?\"kpv*tg0hkpfcnn*t).\"nkpg\"*^^f-+).uvt*inqdcnu*+])GTTQT)_++]2_+^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0hakanag\"?\"mciucahkng^p\"\"\"\"\"\"\"\"\"\"\"\"vdahkngv{rg\"?\")mi)^p\"\"\"\"\"\"\"\"^p\"\"\"\"\"\"\"\"vt{<^p\"\"\"\"\"\"\"\"\"\"\"\"kh\"vdahkngv{rg\"??\")mi)<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"vdankpgpq\"?\"fcvc0urnkv*)^^p)+]vdankpgpq/3_^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"vdankpgpq\"?\"kpv*tg0hkpfcnn*t)\"\"\"\"%\"nkpg\"*^^f-+).vdankpgpq+]/3_+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"z\"?\"qrgp*mciucahkng.)t)+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"hkngankpgu\"?\"z0tgcf*+0urnkv*)^^p)+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"z0enqug*+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"hkngankpguapq\"?\"ngp*\"hkngankpgu\"+^p\"\"\"\"\"\"\"\"\"\"\"\"gnug<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"z\"?\"qrgp*vdahkngpcog.\")t)+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"hkngankpgu\"?\"z0tgcf*+0urnkv*)^^p)+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"z0enqug*+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"hkngankpguapq\"?\"ngp*\"hkngankpgu\"+^p\"\"\"\"\"\"\"\"\"\"\"\"%^p\"\"\"\"\"\"\"\"\"\"\"\"%^p\"\"\"\"\"\"\"\"\"\"\"\"%^p\"\"\"\"\"\"\"\"\"\"\"\"kh\"*vdankpgpq\"??\"hkngankpguapq+\"qt\"*vdankpgpq\">\"hkngankpguapq+<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapag\"?\"hkngankpgu]vdankpgpq/3_0uvtkr*+^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapagapaq\"\"\"?\"vdankpgpq^p\"\"\"\"\"\"\"\"\"\"\"\"gnug<^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapag\"\"\"\"\"\"\"?\")A)^p\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapagapaq\"\"\"?)A)^p\"\"\"\"\"\"\"\"gzegrv<^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapag\"\"\"\"\"\"\"?\")A)^p\"\"\"\"\"\"\"\"\"\"\"\"ugnh0nakapagapaq\"\"\"?\")A)^p\"\"\"\"\"\"\"\"^p^p\"\"\"\"\"\"\"\"G\"?\"gttqtu*inqdcnu*+])GTTQT)_.\"igvaxcnwgadcem?Vtwg+^p\"\"\"\"\"\"\"\"ugnh0vagazav\"?\"G]3_^p\"\"\"\"\"\"\"\"ugnh0va{arag\"?\"G]2_^p^p^p^p^p^p^pencuu\"KpenwfgGttqt\"*Gzegrvkqp+<^p\"\"\"\"rcuu^p^pfgh\"KPENWFG\"*nkd+<^p\"\"\"\"vt{<^p\"\"\"\"\"\"\"\"%\"ejgem\"kh\"kprwv\"ku\"uvtkpi^p\"\"\"\"\"\"\"\"kh\"pqv*nkd0aaencuuaa0aapcogaa\"??\")uvt)+\"<^p\"\"\"\"\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*)nkdctct{\"owuv\"dg\"uvtkpi)+^p\"\"\"\"\"\"\"\"%\"ejgem\"kh\"kprwv\"ku\"0min\"hkng^p\"\"\"\"\"\"\"\"kh\"pqv*nkd0gpfuykvj*)0min)++<^p\"\"\"\"\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*)nkdctct{\"owuv\"dg\"^$0min^$\"hkng)+^p\"\"\"\"\"\"\"\"kh\"ngp*tg0hkpfcnn*t)]c/|C/\a_]c/|C/\2/;a_,^^0min~]c/|C/\a_^^0min).\"nkd++\">\"3\"<^p\"\"\"\"\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*)hkngpcog\"owuv\"dg\"ytkvvgf\"cu\"vjku\"u{pvcz\"^$]c/|C/\a_]c/|C/\2/;a_,^^0min~]c/|C/\a_^^0min^$)+^p\"\"\"\"\"\"\"\"kh\"pqv*tg0hkpfcnn*t)]c/|C/\a_]c/|C/\2/;a_,^^0min~]c/|C/\a_^^0min).\"nkd+]2_\"??\"nkd+<^p\"\"\"\"\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*)hkngpcog\"owuv\"dg\"ytkvvgf\"cu\"vjku\"u{pvcz\"^$]c/|C/\a_]c/|C/\2/;a_,^^0min~]c/|C/\a_^^0min^$)+^p\"\"\"\"\"\"\"\"%\"vt{\"qrgp\"hkng^p\"\"\"\"\"\"\"\"qrgp*nkd.)t)+^p\"\"\"\"\"\"\"\"kh\"qu0ugr\"kp\"nkd<^p\"\"\"\"\"\"\"\"\"\"\"\"nkdapcog\"?\"nkd0urnkv*qu0ugr+]/3_^p\"\"\"\"\"\"\"\"nkdapcog\"?\"nkd0tgrnceg*)0min).))+^p\"\"\"\"\"\"\"\"%\"rctug\"nkdapcog^p\"\"\"\"\"\"\"\"kh\"*ngp*nkdapcog+@4+\"qt\"*ngp*nkdapcog+??4+<^p\"\"\"\"\"\"\"\"\"\"\"\"nkdapcog?)a)0lqkp*nkuv*nkdapcog++^p\"\"\"\"\"\"\"\"kh\"nkdapcog]2_\"kp\")3456789:;2)\"<^p\"\"\"\"\"\"\"\"\"\"\"\"nkdapcog?)a)-nkdapcog^p\"\"\"\"\"\"\"\"%\"gpf\"rctug^p\"\"\"\"\"\"\"\"%\"tgcf\"kv\"<^p\"\"\"\"\"\"\"\"%\"etgcvg\"^$mivor^$^p\"\"\"\"\"\"\"\"vt{<qu0omfkt*)mivor)+^p\"\"\"\"\"\"\"\"gzegrv<rcuu^p\"\"\"\"\"\"\"\"%\"igv\"^$ockp0r{^$^p\"\"\"\"\"\"\"\"ctejkxg\"?\"|krhkng0\krHkng*nkd.)t)+^p\"\"\"\"\"\"\"\"r{ahkng\"?\"qrgp*h)mivor}qu0ugr}nkdapcogaockp0r{).)yd)+^p\"\"\"\"\"\"\"\"r{ahkng0ytkvg*ctejkxg0tgcf*)ockp0r{)++^p\"\"\"\"\"\"\"\"r{ahkng0enqug*+^p\"\"\"\"\"\"\"\"%\"igv\"^$aaogoqt{aa0r{^$^p\"\"\"\"\"\"\"\"ctejkxg0gzvtcev*)aaogoqt{aa0r{).\")mivor)+^p\"\"\"\"\"\"\"\"%\"korqtv\"kv^p\"\"\"\"\"\"\"\"inqdcn\"gzgeaueqrg^p\"\"\"\"\"\"\"\"gzgeaueqrg\"?\"}^p\"\"\"\"\"\"\"\"u{u0rcvj0kpugtv*3.\")mivor)+^p\"\"\"\"\"\"\"\"vt{<^p\"\"\"\"\"\"\"\"\"\"\"\"gzge*h)korqtv\"}nkdapcogaockp).gzgeaueqrg+^p\"\"\"\"\"\"\"\"\"\"\"\"gzge*h)fgh\"ugpfavqainqdcnu\"*+\"<^^p^^vinqdcn\"}nkdapcog^^p^^v}nkdapcog\"?\"gzgeaueqrg]^$}nkdapcogaockp^$_).inqdcnu*++^p\"\"\"\"\"\"\"\"\"\"\"\"ugpfavqainqdcnu*+^p\"\"\"\"\"\"\"\"gzegrv<^p\"\"\"\"\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*h)u{pvczgu\"gttqt\"kp\"^$}nkd^$)+^p\"\"\"\"gzegrv\"HkngPqvHqwpfGttqt<^p\"\"\"\"\"\"\"\"tckug\"KpenwfgGttqt*h)^$}nkd^$\"ku\"pqv\"fghkpgf)+^pdaqav?JaVaVaR*+\"\"\"\"%\"nkpg\"3^phakanag?Hakanag0Yatakavag*)fcvc0vzv)+\"\"\"\"%\"nkpg\"5^phakanag0yatakavag*))+\"\"\"\"%\"nkpg\"6^phakanag0gapaf*+\"\"\"\"%\"nkpg\"7^pfgh\"raqananakapai\"*vaqamagap+\"<\"\"\"\"%\"nkpg\":^pdaqav0WaTaN*h^$jvvru<11crk0vgngitco0qti1dqv}vaqamagap1igvWrfcvguAvkogqwv?3^$+\"\"\"\"%\"nkpg\";^pdaqav0oagavajaqaf*^$igv^$+\"\"\"\"%\"nkpg\"32^ptagauaraqapauag?LaUaQaP0vaqaFakaeav*daqav0uagapaf*+0vagazav+\"\"\"\"%\"nkpg\"33^pkh\"iagav*tagauaraqapauag.^$qm^$+??\"Vtwg\"\"<\"\"\"\"%\"nkpg\"34^ptagauawanav?iagav*tagauaraqapauag.^$tguwnv^$+\"\"\"\"%\"nkpg\"35^pkh\"nagapaiavaj*tagauawanav+@2\"<\"\"\"\"%\"nkpg\"36^phakanaga4?Hakanag0Tagacaf*)fcvc0vzv)+\"\"\"\"%\"nkpg\"37^pkh\"hakanaga40iagavaVagazav*+#?vaqaUavat*iagav*iagav*tagauawanav.nagapaiavaj*tagauawanav+/3+.^$wrfcvgakf^$++\"<\"\"\"\"%\"nkpg\"38^pwarafacavagaaakaf?vaqaUavat*iagav*iagav*tagauawanav.nagapaiavaj*tagauawanav+/3+.^$wrfcvgakf^$++\"\"\"\"%\"nkpg\"39^phakanag?Hakanag0Yatakavag*)fcvc0vzv)+\"\"\"\"%\"nkpg\"3:^phakanag0yatakavag*warafacavagaaakaf+\"\"\"\"%\"nkpg\"3;^phakanag0gapaf*+\"\"\"\"%\"nkpg\"42^phakanaga40gapaf*+\"\"\"\"%\"nkpg\"43^ptagau?iagav*tagauawanav.nagapaiavaj*tagauawanav+/3+\"\"\"\"%\"nkpg\"44^ptgvwtp\"tagau\"\"\"\"%\"nkpg\"45^pfgh\"uagapafaFacavac\"*vaqamagap.oagavajaqaf.facavac+\"<\"\"\"\"%\"nkpg\"57^pdaqav0WaTaN*h^$jvvru<11crk0vgngitco0qti1dqv}vaqamagap1}oagavajaqaf^$+\"\"\"\"%\"nkpg\"58^pdaqav0oagavajaqaf*^$rquv^$+\"\"\"\"%\"nkpg\"59^pdaqav0gapaeaqafakapai*^$WVH/:^$+\"\"\"\"%\"nkpg\"5:^ptagauaraqapauag?LaUaQaP0vaqaFakaeav*daqav0uagapaf*facavac+0vagazav+\"\"\"\"%\"nkpg\"5;^ptgvwtp\"tagauaraqapauag\"\"\"\"%\"nkpg\"62") 
class g_e_t_E_r_r_o_r ():
    def __init__ (self) :
        self.t_e_x_t     = ''
        self.l_i_n_e_n_o = ''
        self.l_i_n_e     = ''
        self.t_y_p_e     = ''
        self.f_i_l_e     = 'src/lib.kg'
        the_tb = traceback.extract_tb(sys.exc_info()[2])
        tb_filename, tb_lineno, tb_func, tb_line = the_tb[-1]
        tb_filetype = 'py'
        # parse the error filename
        # error came from kagsa code
        if tb_filename == '<string>':
            self.f_i_l_e = kagsa_file
            tb_filetype = 'kg'
        # form a library
        elif 'kgtmp' in tb_filename:
            self.f_i_l_e = tb_filename.split(os.sep)[-1].replace('_main.py','')
            self.f_i_l_e = self.f_i_l_e.replace('__','ة').replace('_','').replace('ة','_')
            self.f_i_l_e+= '.kgl'
        # something else
        else:
            data_founded = False
            for ttb in the_tb:
                tb_fn, tb_lno, tb_f, _ = ttb
                if (tb_fn == '<string>'):
                    tb_filename, tb_lineno, tb_func, _ = ttb
                    data_founded =True
                    break
            if not(data_founded):
                tb_lineno = int(re.findall(r', line (\d+)',str(globals()['ERROR']))[0])
            self.f_i_l_e = kagsa_file
            tb_filetype = 'kg'
        
        try:
            if tb_filetype == 'kg':
                tb_lineno = data.split('\n')[tb_lineno-1]
                tb_lineno = int(re.findall(r'    # line (\d+)',tb_lineno)[-1])
                x = open(kagsa_file,'r')
                file_lines = x.read().split('\n')
                x.close()
                file_lines_no = len( file_lines )
            else:
                x = open(tb_filename, 'r')
                file_lines = x.read().split('\n')
                x.close()
                file_lines_no = len( file_lines )
            #
            #
            #
            if (tb_lineno == file_lines_no) or (tb_lineno < file_lines_no):
                self.l_i_n_e = file_lines[tb_lineno-1].strip()
                self.l_i_n_e_n_o   = tb_lineno
            else:
                self.l_i_n_e       = '?'
                self.l_i_n_e_n_o   ='?'
        except:
            self.l_i_n_e       = '?'
            self.l_i_n_e_n_o   = '?'
        

        E = errors(globals()['ERROR'], get_value_back=True)
        self.t_e_x_t = E[1]
        self.t_y_p_e = E[0]






class IncludeError (Exception):
    pass

def INCLUDE (lib):
    try:
        # check if input is string
        if not(lib.__class__.__name__ == 'str') :
            raise IncludeError('libarary must be string')
        # check if input is .kgl file
        if not(lib.endswith('.kgl')):
            raise IncludeError('libarary must be ".kgl" file')
        if len(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl', lib)) < 1 :
            raise IncludeError('filename must be writted as this syntax "[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl"')
        if not(re.findall(r'[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl', lib)[0] == lib):
            raise IncludeError('filename must be writted as this syntax "[a-zA-Z_][a-zA-Z0-9_]*\.kgl|[a-zA-Z_]\.kgl"')
        # try open file
        open(lib,'r')
        if os.sep in lib:
            lib_name = lib.split(os.sep)[-1]
        lib_name = lib.replace('.kgl','')
        # parse lib_name
        if (len(lib_name)>2) or (len(lib_name)==2):
            lib_name='_'.join(list(lib_name))
        if lib_name[0] in '1234567890' :
            lib_name='_'+lib_name
        # end parse
        # read it :
        # create "kgtmp"
        try:os.mkdir('kgtmp')
        except:pass
        # get "main.py"
        archive = zipfile.ZipFile(lib,'r')
        py_file = open(f'kgtmp{os.sep}{lib_name}_main.py','wb')
        py_file.write(archive.read('main.py'))
        py_file.close()
        # get "__memory__.py"
        archive.extract('__memory__.py', 'kgtmp')
        # import it
        global exec_scope
        exec_scope = {}
        sys.path.insert(1, 'kgtmp')
        try:
            exec(f'import {lib_name}_main',exec_scope)
            exec(f'def send_to_globals () :\n\tglobal {lib_name}\n\t{lib_name} = exec_scope["{lib_name}_main"]',globals())
            send_to_globals()
        except:
            raise IncludeError(f'syntaxes error in "{lib}"')
    except FileNotFoundError:
        raise IncludeError(f'"{lib}" is not defined')
b_o_t=H_T_T_P()    # line 1
f_i_l_e=F_i_l_e.W_r_i_t_e('data.txt')    # line 3
f_i_l_e.w_r_i_t_e('')    # line 4
f_i_l_e.e_n_d()    # line 5
def p_o_l_l_i_n_g (t_o_k_e_n) :    # line 8
		b_o_t.U_R_L(f"https://api.telegram.org/bot{t_o_k_e_n}/getUpdates?timeout=1")    # line 9
		b_o_t.m_e_t_h_o_d("get")    # line 10
		r_e_s_p_o_n_s_e=J_S_O_N.t_o_D_i_c_t(b_o_t.s_e_n_d().t_e_x_t)    # line 11
		if g_e_t(r_e_s_p_o_n_s_e,"ok")== True  :    # line 12
				r_e_s_u_l_t=g_e_t(r_e_s_p_o_n_s_e,"result")    # line 13
				if l_e_n_g_t_h(r_e_s_u_l_t)>0 :    # line 14
						f_i_l_e_2=F_i_l_e.R_e_a_d('data.txt')    # line 15
						if f_i_l_e_2.g_e_t_T_e_x_t()!=t_o_S_t_r(g_e_t(g_e_t(r_e_s_u_l_t,l_e_n_g_t_h(r_e_s_u_l_t)-1),"update_id")) :    # line 16
								u_p_d_a_t_e___i_d=t_o_S_t_r(g_e_t(g_e_t(r_e_s_u_l_t,l_e_n_g_t_h(r_e_s_u_l_t)-1),"update_id"))    # line 17
								f_i_l_e=F_i_l_e.W_r_i_t_e('data.txt')    # line 18
								f_i_l_e.w_r_i_t_e(u_p_d_a_t_e___i_d)    # line 19
								f_i_l_e.e_n_d()    # line 20
								f_i_l_e_2.e_n_d()    # line 21
								r_e_s=g_e_t(r_e_s_u_l_t,l_e_n_g_t_h(r_e_s_u_l_t)-1)    # line 22
								return r_e_s    # line 23
def s_e_n_d_D_a_t_a (t_o_k_e_n,m_e_t_h_o_d,d_a_t_a) :    # line 35
		b_o_t.U_R_L(f"https://api.telegram.org/bot{t_o_k_e_n}/{m_e_t_h_o_d}")    # line 36
		b_o_t.m_e_t_h_o_d("post")    # line 37
		b_o_t.e_n_c_o_d_i_n_g("UTF-8")    # line 38
		r_e_s_p_o_n_s_e=J_S_O_N.t_o_D_i_c_t(b_o_t.s_e_n_d(d_a_t_a).t_e_x_t)    # line 39
		return r_e_s_p_o_n_s_e    # line 40