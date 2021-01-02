# Generated by Django 3.1.3 on 2020-12-28 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0031_nota_corretora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='corretora',
            field=models.CharField(blank=True, choices=[('AGORA CTVM S.A.', 'AGORA CTVM S.A.'), ('ALFA CCVM S.A.', 'ALFA CCVM S.A.'), ('AMARIL FRANKLIN CTV LTDA', 'AMARIL FRANKLIN CTV LTDA'), ('ANDBANK DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.', 'ANDBANK DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.'), ('ATIVA INVESTIMENTOS S.A. C.T.C.V.', 'ATIVA INVESTIMENTOS S.A. C.T.C.V.'), ('AZIMUT BRASIL DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.', 'AZIMUT BRASIL DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.'), ('BANCO ABC BRASIL S/A', 'BANCO ABC BRASIL S/A'), ('BANCO ABN AMRO S.A.', 'BANCO ABN AMRO S.A.'), ('BANCO ANDBANK (BRASIL) S.A. ', 'BANCO ANDBANK (BRASIL) S.A. '), ('BANCO B3 S.A.', 'BANCO B3 S.A.'), ('BANCO BARI DE INVESTIMENTOS E FINANCIAMENTOS S.A ', 'BANCO BARI DE INVESTIMENTOS E FINANCIAMENTOS S.A '), ('BANCO BNP PARIBAS BRASIL S/A', 'BANCO BNP PARIBAS BRASIL S/A'), ('BANCO BOCOM BBM S.A. ', 'BANCO BOCOM BBM S.A. '), ('BANCO BRADESCO S.A.', 'BANCO BRADESCO S.A.'), ('BANCO BTG PACTUAL S/A', 'BANCO BTG PACTUAL S/A'), ('BANCO C6 S.A.', 'BANCO C6 S.A.'), ('BANCO CAIXA GERAL - BRASIL S/A', 'BANCO CAIXA GERAL - BRASIL S/A'), ('BANCO CITIBANK S.A ', 'BANCO CITIBANK S.A '), ('BANCO CLÁSSICO S.A.', 'BANCO CLÁSSICO S.A.'), ('BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB', 'BANCO COOPERATIVO DO BRASIL S.A. - BANCOOB'), ('BANCO COOPERATIVO SICREDI S.A.', 'BANCO COOPERATIVO SICREDI S.A.'), ('BANCO CREDIT AGRICOLE BRASIL S/A', 'BANCO CREDIT AGRICOLE BRASIL S/A'), ('BANCO CREDIT SUISSE (BRASIL) S.A.', 'BANCO CREDIT SUISSE (BRASIL) S.A.'), ('BANCO DAYCOVAL S.A.', 'BANCO DAYCOVAL S.A.'), ('BANCO DE INVESTIMENTOS CREDIT SUISSE (BRASIL) S/A', 'BANCO DE INVESTIMENTOS CREDIT SUISSE (BRASIL) S/A'), ('BANCO DO BRASIL S.A.', 'BANCO DO BRASIL S.A.'), ('BANCO DO ESTADO DO PARÁ S/A.', 'BANCO DO ESTADO DO PARÁ S/A.'), ('BANCO DO ESTADO DO RIO GRANDE DO SUL SA', 'BANCO DO ESTADO DO RIO GRANDE DO SUL SA'), ('BANCO DO NORDESTE DO BRASIL SA', 'BANCO DO NORDESTE DO BRASIL SA'), ('BANCO FATOR S/A', 'BANCO FATOR S/A'), ('BANCO FIBRA SA', 'BANCO FIBRA SA'), ('BANCO FINAXIS S.A.', 'BANCO FINAXIS S.A.'), ('BANCO INDUSTRIAL DO BRASIL', 'BANCO INDUSTRIAL DO BRASIL'), ('BANCO INDUSVAL S.A.', 'BANCO INDUSVAL S.A.'), ('BANCO J.P. MORGAN S.A.', 'BANCO J.P. MORGAN S.A.'), ('BANCO KDB DO BRASIL S.A.', 'BANCO KDB DO BRASIL S.A.'), ('BANCO MODAL S.A. ', 'BANCO MODAL S.A. '), ('BANCO NACIONAL DE DESENVOLVIMENTO ECONÔMICO E SOCIAL - BNDES', 'BANCO NACIONAL DE DESENVOLVIMENTO ECONÔMICO E SOCIAL - BNDES'), ('BANCO ORIGINAL S.A.', 'BANCO ORIGINAL S.A.'), ('BANCO OURINVEST S.A.', 'BANCO OURINVEST S.A.'), ('BANCO PAN SA', 'BANCO PAN SA'), ('BANCO PAULISTA S.A.', 'BANCO PAULISTA S.A.'), ('BANCO PINE S/A', 'BANCO PINE S/A'), ('BANCO SAFRA S/A', 'BANCO SAFRA S/A'), ('BANCO SANTANDER (BRASIL) S.A.', 'BANCO SANTANDER (BRASIL) S.A.'), ('BANCO SOCIETE GENERALE BRASIL S.A.', 'BANCO SOCIETE GENERALE BRASIL S.A.'), ('BANCO SOFISA SA', 'BANCO SOFISA SA'), ('BANCO SUMITOMO MITSUI BRASILEIRO S.A.', 'BANCO SUMITOMO MITSUI BRASILEIRO S.A.'), ('BANCO VOTORANTIM SA', 'BANCO VOTORANTIM SA'), ('BANESTES SA BANCO DO ESTADO DO ESPIRITO SANTO', 'BANESTES SA BANCO DO ESTADO DO ESPIRITO SANTO'), ('BANK OF AMERICA MERRILL LYNCH BANCO MULTIPLO S.A.', 'BANK OF AMERICA MERRILL LYNCH BANCO MULTIPLO S.A.'), ('BANRISUL S.A. CORRETORA DE VALORES MOBILIÁRIOS E CÂMBIO', 'BANRISUL S.A. CORRETORA DE VALORES MOBILIÁRIOS E CÂMBIO'), ('BB BANCO DE INVESTIMENTO S.A.', 'BB BANCO DE INVESTIMENTO S.A.'), ('BGC LIQUIDEZ DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.', 'BGC LIQUIDEZ DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.'), ('BNY MELLON BANCO S.A.', 'BNY MELLON BANCO S.A.'), ('BOCOM BBM CCVM S.A.', 'BOCOM BBM CCVM S.A.'), ('BR PARTNERS BANCO DE INVESTIMENTO S.A.', 'BR PARTNERS BANCO DE INVESTIMENTO S.A.'), ('BR-CAPITAL DTVM S.A.', 'BR-CAPITAL DTVM S.A.'), ('BRADESCO S/A CTVM', 'BRADESCO S/A CTVM'), ('BRB DTVM SA', 'BRB DTVM SA'), ('BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.', 'BRL TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.'), ('BS2 DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'BS2 DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('BTG PACTUAL CTVM S/A', 'BTG PACTUAL CTVM S/A'), ('C6 CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.', 'C6 CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.'), ('CA INDOSUEZ WEALTH (BRAZIL) S.A. DTVM', 'CA INDOSUEZ WEALTH (BRAZIL) S.A. DTVM'), ('CAIXA ECONOMICA FEDERAL', 'CAIXA ECONOMICA FEDERAL'), ('CITIBANK DTVM SA', 'CITIBANK DTVM SA'), ('CITIBANK N.A.', 'CITIBANK N.A.'), ('CITIGROUP GLOBAL MARKETS BRASIL, CCTVM S/A', 'CITIGROUP GLOBAL MARKETS BRASIL, CCTVM S/A'), ('CM CAPITAL MARKETS CCTVM LTDA', 'CM CAPITAL MARKETS CCTVM LTDA'), ('CODEPE CORRETORA DE VALORES E CÂMBIO S.A.', 'CODEPE CORRETORA DE VALORES E CÂMBIO S.A.'), ('COINVALORES CCVM LTDA', 'COINVALORES CCVM LTDA'), ('CORRETORA GERAL DE VALORES E CAMBIO LTDA', 'CORRETORA GERAL DE VALORES E CAMBIO LTDA'), ('CREDIT SUISSE (BRASIL) S/A CTVM', 'CREDIT SUISSE (BRASIL) S/A CTVM'), ('CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.', 'CREDIT SUISSE HEDGING-GRIFFO CORRETORA DE VALORES S.A.'), ('CUSTODIANTE EXCLUSIVO DE TÍTULOS PÚBLICOS', 'CUSTODIANTE EXCLUSIVO DE TÍTULOS PÚBLICOS'), ('DEUTSCHE BANK SA - BANCO ALEMAO', 'DEUTSCHE BANK SA - BANCO ALEMAO'), ('EASYNVEST - TÍTULO CORRETORA DE VALORES SA', 'EASYNVEST - TÍTULO CORRETORA DE VALORES SA'), ('ELITE CCVM LTDA', 'ELITE CCVM LTDA'), ('FATOR S.A. CORRETORA DE VALORES', 'FATOR S.A. CORRETORA DE VALORES'), ('FRAM CAPITAL DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.', 'FRAM CAPITAL DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A.'), ('GENIAL INSTITUCIONAL CORRETORA DE CAMBIO, TITULOS E VALORES MOBILIARIOS S.A.', 'GENIAL INSTITUCIONAL CORRETORA DE CAMBIO, TITULOS E VALORES MOBILIARIOS S.A.'), ('GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.', 'GENIAL INVESTIMENTOS CORRETORA DE VALORES MOBILIÁRIOS S.A.'), ('GOLDMAN SACHS DO BRASIL CTVM S/A', 'GOLDMAN SACHS DO BRASIL CTVM S/A'), ('GUIDE INVESTIMENTOS S.A. CORRETORA DE VALORES', 'GUIDE INVESTIMENTOS S.A. CORRETORA DE VALORES'), ('H.COMMCOR DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.', 'H.COMMCOR DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA.'), ('HAITONG BANCO DE INVESTIMENTO DO BRASIL S.A.', 'HAITONG BANCO DE INVESTIMENTO DO BRASIL S.A.'), ('HAITONG SECURITIES DO BRASIL CORRETORA DE CÂMBIO E VALORES MOBILIÁRIOS S.A.', 'HAITONG SECURITIES DO BRASIL CORRETORA DE CÂMBIO E VALORES MOBILIÁRIOS S.A.'), ('ICAP DO BRASIL CTVM LTDA', 'ICAP DO BRASIL CTVM LTDA'), ('ID CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'ID CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('IDEAL CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'IDEAL CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('ÍNDIGO INVESTIMENTOS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA', 'ÍNDIGO INVESTIMENTOS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA'), ('INTER DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS', 'INTER DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS'), ('INTL FCSTONE DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA', 'INTL FCSTONE DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA'), ('INTRADER DTVM LTDA', 'INTRADER DTVM LTDA'), ('ITAÚ CORRETORA DE VALORES S.A. ', 'ITAÚ CORRETORA DE VALORES S.A. '), ('ITAÚ DTVM S.A. ', 'ITAÚ DTVM S.A. '), ('ITAU UNIBANCO S.A.', 'ITAU UNIBANCO S.A.'), ('J P MORGAN S/A DTVM', 'J P MORGAN S/A DTVM'), ('J. P. MORGAN CCVM S.A.', 'J. P. MORGAN CCVM S.A.'), ('LECCA DTVM LTDA.', 'LECCA DTVM LTDA.'), ('LEROSA S/A CORRETORA DE VALORES E CÂMBIO', 'LEROSA S/A CORRETORA DE VALORES E CÂMBIO'), ('LIMINE TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.', 'LIMINE TRUST DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.'), ('MAGLIANO S/A C.C.V.M.', 'MAGLIANO S/A C.C.V.M.'), ('MAXIMA S/A CCTVM', 'MAXIMA S/A CCTVM'), ('MERCANTIL DO BRASIL CORRETORA S/A CTVM', 'MERCANTIL DO BRASIL CORRETORA S/A CTVM'), ('MERRILL LYNCH S/A CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS', 'MERRILL LYNCH S/A CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS'), ('MIRAE ASSET WEALTH MANAGEMENT (BRAZIL) CCTVM LTDA', 'MIRAE ASSET WEALTH MANAGEMENT (BRAZIL) CCTVM LTDA'), ('MODAL D.T.V.M. LTDA', 'MODAL D.T.V.M. LTDA'), ('MORGAN STANLEY CTVM S.A.', 'MORGAN STANLEY CTVM S.A.'), ('MUNDINVEST S/A CCVM', 'MUNDINVEST S/A CCVM'), ('NECTON INVESTIMENTOS S.A. CORRETORA DE VALORES MOBILIÁRIOS E COMMODITIES', 'NECTON INVESTIMENTOS S.A. CORRETORA DE VALORES MOBILIÁRIOS E COMMODITIES'), ('NOVA FUTURA CTVM LTDA', 'NOVA FUTURA CTVM LTDA'), ('NOVINVEST CORRETORA DE VALORES MOBILIÁRIOS LTDA.', 'NOVINVEST CORRETORA DE VALORES MOBILIÁRIOS LTDA.'), ('OLIVEIRA TRUST DTVM S.A.', 'OLIVEIRA TRUST DTVM S.A.'), ('ÓRAMA DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'ÓRAMA DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('ORLA DTVM S.A.', 'ORLA DTVM S.A.'), ('OURINVEST DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'OURINVEST DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('PI DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'PI DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('PINE INVESTIMENTOS DTVM LTDA', 'PINE INVESTIMENTOS DTVM LTDA'), ('PLANNER CORRETORA DE VALORES SA', 'PLANNER CORRETORA DE VALORES SA'), ('PLANNER TRUSTEE DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.', 'PLANNER TRUSTEE DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.'), ('PLURAL S.A. BANCO MULTIPLO', 'PLURAL S.A. BANCO MULTIPLO'), ('RB CAPITAL INVESTIMENTOS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA', 'RB CAPITAL INVESTIMENTOS DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA'), ('REAG DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'REAG DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('RENASCENCA DTVM LTDA', 'RENASCENCA DTVM LTDA'), ('RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA', 'RJI CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS LTDA'), ('SAFRA CORRETORA DE VALORES E CÂMBIO LTDA. ', 'SAFRA CORRETORA DE VALORES E CÂMBIO LTDA. '), ('SANTANDER CACEIS BRASIL DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A ', 'SANTANDER CACEIS BRASIL DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS S.A '), ('SANTANDER CCVM S/A', 'SANTANDER CCVM S/A'), ('SENSO CORRETORA DE CÂMBIO E VALORES MOBILIÁRIOS S.A ', 'SENSO CORRETORA DE CÂMBIO E VALORES MOBILIÁRIOS S.A '), ('SINGULARE CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A. ', 'SINGULARE CORRETORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A. '), ('SITA SOCIEDADE CCVM S.A.', 'SITA SOCIEDADE CCVM S.A.'), ('SLW CVC LTDA', 'SLW CVC LTDA'), ('SOLIDEZ - CORRETORA DE CÂMBIO, TÍTULOS E VALORES MOBILIÁRIOS LIMITADA', 'SOLIDEZ - CORRETORA DE CÂMBIO, TÍTULOS E VALORES MOBILIÁRIOS LIMITADA'), ('SOLIDUS SA CCVM', 'SOLIDUS SA CCVM'), ('TERRA INVESTIMENTOS DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA', 'TERRA INVESTIMENTOS DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA'), ('TORO CORRETORA DE TÍTULOS E VALORES MOBILIARIOS LTDA', 'TORO CORRETORA DE TÍTULOS E VALORES MOBILIARIOS LTDA'), ('TRINUS CAPITAL DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'TRINUS CAPITAL DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('TULLETT PREBON BRASIL CORRETORA DE VALORES E CÂMBIO LTDA', 'TULLETT PREBON BRASIL CORRETORA DE VALORES E CÂMBIO LTDA'), ('UBS BRASIL BANCO DE INVESTIMENTO S.A.', 'UBS BRASIL BANCO DE INVESTIMENTO S.A.'), ('UBS BRASIL CORRETORA DE CAMBIO, TITULOS E VALORES MOBILIARIOS S.A.', 'UBS BRASIL CORRETORA DE CAMBIO, TITULOS E VALORES MOBILIARIOS S.A.'), ('VIC DTVM S/A', 'VIC DTVM S/A'), ('VITREO DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.', 'VITREO DISTRIBUIDORA DE TÍTULOS E VALORES MOBILIÁRIOS S.A.'), ('VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.', 'VORTX DISTRIBUIDORA DE TITULOS E VALORES MOBILIARIOS LTDA.'), ('VOTORANTIM ASSET MANAGEMENT DTVM LTDA.', 'VOTORANTIM ASSET MANAGEMENT DTVM LTDA.'), ('WARREN CORRETORA DE VALORES MOBILIÁRIOS E CÂMBIO LTDA. ', 'WARREN CORRETORA DE VALORES MOBILIÁRIOS E CÂMBIO LTDA. '), ('XP INVESTIMENTOS CCTVM S.A.', 'XP INVESTIMENTOS CCTVM S.A.')], max_length=250),
        ),
    ]
