from datetime import datetime, timedelta

data_hoje = datetime.now()
data_futura = data_hoje + timedelta(2)

print(f'A data de hoje é  {data_hoje.date()} e daqui a dois dias será {data_futura.date()}')

