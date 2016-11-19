YASHA=	yasha --no-extensions -v appmate.yml

.SUFFIXES: .py .py.jinja

.py.jinja.py:
	${YASHA} -o ${.TARGET} ${.IMPSRC}

all: admin.py apps.py filters.py models.py routers.py serializers.py views.py
