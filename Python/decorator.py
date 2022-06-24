def step1(p1):
    p1 = f'--{p1}--'

    def step2(p2):
        return f'{p1} e {p2}'

    return step2


# function_p2 = step1('Open the door')
# print(function_p2('Enter the room'))
# print(step1('Open the door')('Enter the room'))

def verify_logged_user(p_function):
    def verify():
        print('[before lets verify if the user is logged]')
        retorno = p_function()
        print('[END]')
        return retorno
    return verify


@verify_logged_user
def save_post():
    print('...[running]')
    print('Post create!')


save_post()
