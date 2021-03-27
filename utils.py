

def list_to_table(list_str):
    res = '<center><table style="border-collapse: collapse;border: 1px solid black;padding: 5px;">'
    for i in range(len(list_str)):
        res += '<tr style="border-collapse: collapse;border: 1px solid black;padding: 5px;">'
        for j in range(len(list_str[i])):
            color = "skyblue"
            if(list_str[i][j] == 0):
                color = "red"
            res += '<td style="border-collapse: collapse;' +'background:' + color + ';' + 'border: 1px solid black;padding: 5px 10px 5px 10px;">' + str(list_str[i][j]) + '</td>'
        res += '</tr>'
    res += '</table></center>'
    return res