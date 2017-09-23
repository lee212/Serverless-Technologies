

wsk trigger create data-inserted-trigger --feed Bluemix_openwhisk-cloudant_Credentials-1/changes --param dbname "names"

#wsk action invoke --blocking --param name Tahoma --param color Tabby process-change


wsk action create process-change-cloudant-sequence --sequence Bluemix_openwhisk-cloudant_Credentials-1/read,process-change


bx wsk rule create log-change-rule data-inserted-trigger process-change-cloudant-sequence
