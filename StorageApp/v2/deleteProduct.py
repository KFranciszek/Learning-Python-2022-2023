import  json
def delete_product():
    delete_select = input("What product you want  delete: ")

    try:
        with open("prod_list.json", 'r') as f:


            data_open = f.read()
            data_search = json.loads(data_open)

    except FileNotFoundError:
        print("File not found")
        sys.exit(1)

    except  ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed')


    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


    found = False
    delete = ""
    for i in data_search:
        if i["name"] == delete_select:
            delete= (input(f"Are you sure you want to remove {i}  ? "))
            found = True
            if delete == "yes":
               data_search.remove(i)
    with open("prod_list.json", 'w') as f:
        json.dump(data_search,f)

    if not found:
       print("Product dont found")


delete_product()