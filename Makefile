name=
num=

ABCPATH=./ABC/${num}
AGCPATH=./AGC/${num}

.PHONY: abc
abc:
	mkdir ${ABCPATH}
	touch ${ABCPATH}/A.py
	touch ${ABCPATH}/B.py
	touch ${ABCPATH}/C.py
	touch ${ABCPATH}/D.py
	touch ${ABCPATH}/E.py
	touch ${ABCPATH}/F.py

.PHONY: agc
agc:
	mkdir ${AGCPATH}
	touch ${AGCPATH}/A.py
	touch ${AGCPATH}/B.py
	touch ${AGCPATH}/C.py
	touch ${AGCPATH}/D.py
	touch ${AGCPATH}/E.py
	touch ${AGCPATH}/F.py

other:
	mkdir ./${name}/${num}
	touch ./${name}/${num}/A.py
	touch ./${name}/${num}/B.py
	touch ./${name}/${num}/C.py
	touch ./${name}/${num}/D.py
	touch ./${name}/${num}/E.py
	touch ./${name}/${num}/F.py