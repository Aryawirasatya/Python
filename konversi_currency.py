while True:


    #kurs dollar amerika serikat
    kurs_usd = 15685
    usd_to_idr = lambda usd_value : kurs_usd * usd_value
    idr_to_usd = lambda idr_value : kurs_usd / idr_value

    #kurs ringgit malaysia
    kurs_Rm =3320.70
    rm_to_idr = lambda rm_value: kurs_Rm * rm_value
    idr_to_rm = lambda idr_value : kurs_Rm /idr_value

    #kurs euro
    kurs_euro = 16758.4900
    euro_to_idr = lambda euro_value : kurs_euro * euro_value
    idr_to_euro = lambda idr_value : kurs_euro / idr_value
    #kurs singapore dollar
    kurs_dollar_singapore = 11531.68
    sgd_to_idr = lambda sgd_value: kurs_dollar_singapore * sgd_value
    idr_to_sgd = lambda idr_value: kurs_dollar_singapore / idr_value
    # kurs brunei dollar
    kurs_brunei = 11531.68
    bnd_to_idr = lambda bnd_value: kurs_brunei * bnd_value
    idr_to_bnd = lambda idr_value: kurs_brunei / idr_value
    # kurs poundsterling
    kurs_poundsterling = 19176.32
    pounds_to_idr = lambda  pounds_value: kurs_poundsterling * pounds_value
    idr_to_pounds = lambda idr_value: kurs_poundsterling / idr_value
    # kurs china yuan 
    kurs_china_yuan = 2152.38
    cny_to_idr = lambda cny_value: kurs_china_yuan * cny_value
    idr_to_cny = lambda idr_value: kurs_china_yuan / idr_value
    # kurs saudi riyal 
    kurs_saudi_riyal = 4183.00
    sar_to_idr = lambda sar_value: kurs_saudi_riyal * sar_value
    idr_to_sar = lambda idr_value: kurs_brunei / idr_value
    # kurs dollar canada 
    kurs_canada_dollar = 11367.09
    cad_to_idr = lambda cad_value: kurs_canada_dollar * cad_value
    idr_to_cad = lambda idr_value: kurs_canada_dollar / idr_value

    print('\t-----------------------------')
    print('💵 SELAMAT DATANG DI APLIKASI KONVERSI MATA UANG 💵')
    print('\t-----------------------------')


    print('1. USD (USA)')
    print('2. RM (MALAYSIA)')
    print('3. EURO (EUROPA)')
    print('4. SGD (SINGAPORE)')
    print('5. BND (BRUNEI)')
    print('6  POUNDSTERLING')
    print('7. YUAN (CHINA)')
    print('8. SAR (SAUDI ARABIA)')
    print('9. CAD (CANADA)')
    print('-'*45)
    
    currency = int(input('silahkan pilih jenis mata uang : '))

    if currency == 1:
        print('='*45)
        print('\tKONVERSI USD')
        print('1. USD TO IDR')
        print('2. IDR TO USD')
        print('-'*45)
        currency =int(input('silahkan pilih jenis koversi anda : '))

        if currency == 1:
            print('-----USD TO IDR-----')
            usd_value = float(input('silahkan masukan nilai dollar amerika serikat : '))
            usdidr = usd_to_idr (usd_value)
            print(f'hasilnya adalah Rp {usdidr:,.2f} ')
            print('-'*45)


        elif currency == 2:
            print('-----IDR TO USD-----')
            idr_value = float(input('silahkan masukan nilai rupiah : '))
            idrusd = idr_to_usd (idr_value)
            print(f'hasilnya adalah Usd {idrusd:,.2f} ')
            print('-'*45)
        
        else:
            print('maaf,input anda tidak valid')
    elif currency == 2:
        print('='*45)
        print('\tKONVERSI RINGGIT MALAYSIA')
        print('1. RM TO IDR')
        print('2. IDR TO RM')
        print('-'*45)
        
        ans = int(input('silahkan pilih jenis konversi anda : '))

        if ans == 1:
            print('='*45)
            print('-----RM TO IDR-----')
            rm_value = float(input('silahkan masukan nilai ringgit anda : '))
            rmvalue = rm_to_idr(rm_value)
            print(f'hasilnya adalah Rp {rmvalue:,.2f} ')
            print('-'*45)

        elif ans == 2:
            print('='*30)
            print('-----IDR TO RM-----')
            idr_value = float(input('silahkan masukan nilai rupiah anda '))
            idrvalue = idr_to_rm(idr_value)
            print(f'hasilnya adalah Rm {idrvalue:,.2f}')        
            print('-'*45)

        else:
            print('maaf, input anda tidak valid')

    elif currency == 3:
        print('='*45)
        print('\tKONVERSI EURO')
        print('1. EURO TO IDR')
        print('2. IDR TO EURO')

        ans = int(input('silahkan pilih jenis konversi anda : '))
        if ans == 1:
            print('-----EURO TO IDR-----')
            euro_value = float(input('silahkan masukan nilai euro anda : '))
            eurovalue = euro_to_idr( euro_value)
            print(f'hasilnya adalah Rp {eurovalue:,.2f}')
            print('-'*45)
            
        elif ans == 2:
            print('-----IDR TO EURO-----')
            idr_value = float(input('silahkan masukan nilai rupiah anda : '))
            idrvalue = idr_to_euro(idr_value)
            print(f'hasilnya adalah Euro {idrvalue:,.2f}')
            print('-'*45)

        else:
            print('maaf,input anda tidak valid')

    elif currency == 4:
        print('='*45)
        print('\tKONVERSI SGD SINGAPORE')
        print('1. SGD TO IDR')
        print('2. IDR TO SGD')

        ans = int(input('silahkan pilih jenis konversi anda : ')) 
        if ans == 1:
            print('-----SGD TO IDR-----')
            sgd_value = float(input('silahkan masukan nilai singapore dollar anda : '))
            sgdvalue = sgd_to_idr(sgd_value)   
            print(f'hasilnya adalah Rp {sgdvalue:,.2f}')
            print('-'*45)

        elif ans == 2:
            print('='*45)
            print('-----IDR TO SGD-----')
            idr_value = float(input('silahkan masukan nilai rupiah anda : '))
            idrvalue = idr_to_sgd(idr_value)
            print(f'hasilnya adalah SGD {idrvalue:,.2f}')
            print('-'*45)
        
        else:
            print('maaf,input anda tidak valid')
        
    elif currency == 5:
        print('='*45)
        print('\tKONVERSI DOLLAR BRUNEI')
        print('1. BND TO IDR')
        print('2. IDR TO BND')
        ans = int(input('silahkan pilih jenis konversi anda : '))

        if ans == 1:
            print('='*45)
            print('-----BND TO IDR-----')
            bnd_value = float(input('silahkan masukan nilai Dollar Brunei anda : '))
            bndvalue = bnd_to_idr(bnd_value)
            print(f'hasilnya adalah Rp {bndvalue:,.2f}')
            print('-'*45)

        elif ans == 2:
            print('='*45)
            print('IDR TO BND')
            idr_value = float(input('silahkan masukan nilai rupiah anda : '))
            idrvalue = idr_to_bnd(idr_value)
            print(f'hasilnya adalah BND {idrvalue:,.2f}')   
            print('-'* 45)
            
        else:
            print('maaf,input anda tidak valid')
    
    elif currency == 6:
        print('=' *45)
        print('\t KONVERSI POUNDSTERLING')
        print('1. POUNDS TO IDR')
        print('2. IDR TO POUNDS')
        ans = int(input('silahkan pilih jenis konversi anda : '))

        if ans == 1:
            print('='*45)
            print('-----POUNDS TO IDR-----')
            pounds_value = float(input('silahkan masukan nilai POUNDS anda : '))
            poundsvalue = pounds_to_idr(pounds_value)
            print(f'hasilnya adalah Rp {poundsvalue:,.2f}')
            print('-'* 45)

        elif ans == 2:
            print('='*45)
            print('-----IDR TO POUNDSTERLING-----')
            idr_value = float(input('silahkan masukan Nilai Rupiah anda : '))
            idrvalue = idr_to_pounds(idr_value)
            print(f'hasilnya adalah Pounds {idrvalue:,.2f}')
            print('-'*45)
        
        else:
            print('maaf,input anda tidak valid')
    
    elif currency == 7:
        print('='*45)
        print('\t KONVERSI YUAN CHINA')
        print('1. YUAN TO IDR')
        print('2. IDR TO YUAN')
        ans = int(input('silahkan pilih jenis konversi anda : '))

        if ans == 1:
            print('='*45)
            print('-----YUAN TO IDR-----')
            cny_value = float(input('silahkan masukan nilai Yuan anda : '))
            cnyvalue = cny_to_idr(cny_value)
            print(f'hasilnya adalah Rp {cny_value:,.2f}')
            print('-'*45)

        elif ans == 2:
            print('='*45)
            print('-----IDR TO CNY-----')
            idr_value = float(input('hasilnya adalah : '))
            idrvalue = idr_to_cny(idr_value)
            print(f'hasilnya adalah Cny {idr_value:,.2f}')        
            print('-'*45)

        else:
            print('maaf,input anda tidak valid')
            
    elif currency == 8:
        print('='*45)
        print('\tKONVERSI SAUDI RIYAL')
        print('1. SAR TO IDR')
        print('2. IDR TO SAR')
        ans = int(input('silahkan masukan jenis konversi anda : '))

        if ans == 1:
            print('-'*45)
            print('-----SAR TO IDR-----')
            sar_value = float(input('silahkan masukan nilai saudi riyal anda : '))
            sarvalue = sar_to_idr(sar_value)
            print(f'hasilnya adalah Rp {sarvalue:,.2F}')
            print('-'*45)
        
        elif ans == 2:
            print('='*45)
            print('-----IDR TO SAR-----')
            idr_value = float(input('silahkan masukan nilai Rupiah anda : '))
            idrvalue = idr_to_sar(idr_value)
            print(f'hasilnya dalah Sar {idrvalue:,.2f}')
            print('-'*45)

        else:
            print('maaf,input anda tidak valid')

    elif currency == 9:
        print('='*45)
        print('\t KONVERSI CANADA DOLLAR')
        print('1. CAD TO IDR')
        print('2. IDR TO CAD')
        ans = int(input('silahkan pilih jenis konversi anda : '))

        if ans == 1:
            print('-'*45)
            print('-----CAD TO IDR-----')
            cad_value = float(input('silahkan masukan nilai Canada dollar anda : '))
            cadvalue = cad_to_idr(cad_value)
            print(f'hasilnya adalah Rp {cadvalue:,.2f}')
            print('-'*45)

        elif ans == 2:
            print('='*45)
            print('-----IDR TO CAD-----')
            idr_value = float(input('silahkan masukan nilai Rupiah anda : '))
            idrvalue = idr_to_cad(idr_value)
            print(f'hasilnya adalah Cad {idrvalue:,.2f}')

        else:
            print('maaf,input anda tidak valid')
    
    else:
            print('maaf,input anda tidak valid!!!')

    ulang = input('ingin mengulang? {y/n} :')

    if ulang.lower() != 'y':
        break
    
    
    
