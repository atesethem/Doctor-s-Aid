assignment2 = open("doctors_aid_inputs.txt")
output=open("doctors_aid_outputs.txt.txt","w")
list_of_names=[]
thelist=[]
for line in assignment2:
    line= line.replace(" ",",").replace(",,",",")
    line=line.split(",")
    line[-1]=line[-1].replace("\n","")
    thelist.append(line)
k=assignment2.readlines()
print(k)
for line in thelist:
    if line[0]=="create":
        def create():
            if line[1] in list_of_names:
                output.write("Patient " + line[1] + " cannot be recorded due to duplication.\n")
            else:
                list_of_names.append(line[1])
                output.write("Patient " + line[1] + " is recorded.\n")
        create()
    if line[0] == "remove":
        def remove():
            if line[1] not in list_of_names:
                output.write("Patient " + line[1] + " cannot be removed due to absence.")
            else:
                list_of_names.remove(line[1])
                output_1 = "Patient " + line[1] + " is removed.\n"
                output.write(output_1)
        remove()
    if line[0] =="list":
        def list():
            output.write(
                "Patient\tDiagnosis  \t\t\tDisease\t\t\tDisease\t\t\tTreatment\t\tTreatment\nName\tAccuracy  \t\t\tName\t\t\tIncidence\t\tName\t\tRisk\n" + 73 * "-" + "\n")
            for line in thelist:
                if len(line)== 9:
                    treatment_1 = line[6]
                    treatment_2 = line[7]
                    line = line[:6] + [line[8]]
                    line.insert(-1, treatment_1 + treatment_2)
                if line[0] == "create":
                    if line[1] in list_of_names:
                        percentage = float(line[2]) * 100
                        percentage = f"{percentage:.2f}" + "%"
                        percentage_surgery = round(float(line[-1]) * 100)
                        percentage_surgery = str(percentage_surgery) + "%"
                        output.write(
                            line[1] + "\t" + percentage + "  \t\t\t" + line[3] + " " + line[4] + "\t" + line[5] + "\t\t" +
                            line[6] + "\t" + percentage_surgery + "\n")
        list()
    if line[0] =="probability":
        def probability():
            if name in list_of_names:

                for line in thelist:
                    if line[0] == "create" and line[1] == name:
                        result = line[5].split("/")
                        value = ((1 - float(line[2])) * (float(result[1]) - float(result[0]))) + (float(line[2])*float(
                            result[0]))
                        itsprobabilty = (int(result[0])*float(line[2])) / value * 100
                        itsprobabilty = f"{itsprobabilty:.2f}"
                        print(itsprobabilty)
                        if name in list_of_names:
                            output.write("Patient " + line[1] + " has a probability of " + itsprobabilty + "% of having " + line[
                                3] + " " + line[4] + ".\n")
            else:
                output.write("probability for " + name + " cannot be calculated due to absence.\n")
        name=line[1]
        probability()
    if line[0] == "recommendation":
        def recommendation():
            if name in list_of_names:
                for line in thelist:
                    if line[0] == "create" and line[1] == name:
                        result = line[5].split("/")
                        haydar = ((1 - float(line[2])) * (float(result[1]) - float(result[0]))) + float(
                            result[0])
                        recom = int(result[0]) / haydar * 100
                        recom = f"{recom:.2f}"
                        if line[1] in list_of_names:
                            if float(recom) < float(line[-1]) * 100:
                                output.write("System suggests " + name + " NOT to have the treatment.\n")
                            else:
                                output.write("System suggests " + name + " to have the treatment.\n")

            else:
                output.write("Recommendation for " + name + " cannot be calculated due to absence.\n")
        name=line[1]
        recommendation()

