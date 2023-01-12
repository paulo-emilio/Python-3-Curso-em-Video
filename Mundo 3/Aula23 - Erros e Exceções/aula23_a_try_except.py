while True:
    try:
        a = int(input('Numerador: '))
        b = int(input('Denominador: '))
        r = a / b

    except (ValueError, TypeError):
        print('Tivemos um problema com os os tipos de dados que você digitou.')
    except ZeroDivisionError:
        print('Não existe divisão por zero.')
    except KeyboardInterrupt:
        print('\nO usuário preferiu parar o programa.')
        break
    except Exception as erro:
        print(f'Problema encontrado foi {erro.__cause__}')
    except:
        print('Infelizmente tivemos um problema :(')
    else:
        print(f'Resultado: {r:.1f}')
        break
    finally:
        print('-'*66)
