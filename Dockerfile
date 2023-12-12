FROM public.ecr.aws/lambda/python:3.8

# Copy function code
#COPY app.py ${LAMBDA_TASK_ROOT}
#COPY requirements.txt .
COPY . ${LAMBDA_TASK_ROOT}/src/.
COPY requirements.txt ${LAMBDA_TASK_ROOT}/requirements.txt

RUN pip3 install -r requirements.txt --target ${LAMBDA_TASK_ROOT}
#ENV PYTHONUNBUFFERED=TRUE

#ENTRYPOINT ["app.handler"]
CMD ["src/app.handler"]
