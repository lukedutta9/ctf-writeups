# shebang info

cyberyoddha.baycyber.net
1337

# shebang0

ls for hidden files, there's a hidden flag.txt

```
CYCTF{w3ll_1_gu3$$_b@sh_1s_e@zy}
```

# shebang1

grep the flag.txt file for curly brace

```
CYCTF{w3ll_1_gu3$$_y0u_kn0w_h0w_t0_gr3p}
```

# shebang2

cat all files in these directories  grep for CYCTF

```
find . -exec cat {} \; 2>/dev/null | grep CYCTF
```

```
CYCTF{W0w_th@t$_@_l0t_0f_f1l3s}
```

# shebang3

run `diff file.txt file2.txt`
I just manually wrote the flag down, prob a better way

```
CYCTF{SPOT_TH3_D1FF}
```

# shebang4

there's a png file in the folder, scp it out

```
scp -P 1337 shebang4@cyberyoddha.baycyber.net:flag.png .
```
```
CYCTF{W3ll_1_gu3$$_th@t_w@s_actually_easy}
```

# shebang5

desc hints at SUID

first, find all files with the SUID flag in permissions
```
find / -perm -4000 -exec ls -ldb {} \; 2>/dev/null
```

We found a program /var/cat owned by shebang6  the SUID flag, meaning we can run that as shebang6

Look for files owned by shebang6
```
find / -user shebang6 2>/dev/null
```

There's two, /var/cat,  another interesting file

Run `/var/cat /etc/passwords/shebang6`

```
CYCTF{W3ll_1_gu3$$_SU1D_1$_e@$y_fl@g$}
```

# password1

Created script to reverse
```
CYCTF{pu771ng_th3_ch@r@ct3r$_t0g3th3r_1337}
```

# password2

Created script to reverse
```
CYCTF{ju$t_@_l177l3_scr@mbl3_f0r_y0u_t0_d3c0d3}
```

# password3

Created script to reverse
```
```

# overflow1

overflow with AAAAAAAAAAAAAAAAB to get shell
run `cat flag.txt 2>&1`

```
CYCTF{st@ck_0v3rfl0ws_@r3_3z}
```

# overflow2

Run this and pipe into netcat
```
python3 input.py | nc cyberyoddha.baycyber.net 10002
```

# yayrev

first = lgUBAJu0n_y33tRaQ_C
second = EnD_PytHONWh0al3g