with open("haproxy.cnf.now.txt","r") as new:
                            fla=True
                            for i in new:
                                if i.strip()==key1:
                                    fla=False
                                    continue
                                if i.strip().startswith("backend") and fla==False:
                                    fla=True
                                    break
                                if fla==False:
                                    now_list.append(i.strip())