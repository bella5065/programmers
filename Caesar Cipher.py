'''시저 암호'''

def solution(s, n):
    answer = ''
    al_lo = 'abcdefghijklmnopqrstuvwxyz'
    al_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for alpha in s:
        if alpha.isupper() :
            imsi = al_up.index(alpha) + n
            if imsi > len(al_up) -1:
                answer += al_up[imsi - len(al_up)]
            else: answer += al_up[imsi]
        elif alpha.islower() :
            imsi = al_lo.index(alpha) + n
            if imsi > len(al_up) -1:
                answer += al_lo[imsi - len(al_up)]
            else: answer += al_lo[imsi]
        else:
            answer += alpha
    return answer