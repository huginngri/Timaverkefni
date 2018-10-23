def get_filename_from_user(promt):
    file_name = input(promt)
    return file_name

def create_key(name_data):
    last_name, first_name = name_data.split(",")
    full_name = "{} {}".format(first_name.strip(), last_name.strip())
    return full_name

def process_value_data(chess_player_data):
    rank = int(chess_player_data[0])
    country = chess_player_data[2].strip()
    elo_points = int(chess_player_data[3])
    birth_year = int(chess_player_data[4])

    return [rank, country, elo_points, birth_year]

def create_country_dict(chess_player_dict):
    country_dict = {}
    for key, value in chess_player_dict.items():
        country = value[1]
        if country in country_dict:
            country_dict[country].append(key)
        else:
            country_dict[country] = [key]
    return country_dict

def get_data_from_file(file_name):
    chess_player_dict = {}
    try:
        with open(file_name, 'r') as file_content:
            for line in file_content:
                line = line.split(";")
                key = create_key(line[1])
                value = process_value_data(line)
                chess_player_dict[key] = value
    
    except FileNotFoundError:
        pass
    return chess_player_dict

def print_header(header_text):
    print(header_text)
    print("-"*len(header_text))

def print_resault(chess_player_data, country_dict):
    for key, value in sorted(country_dict.items()):
        elo_points_for_player = chess_player_data[name][2]
        avg = 0
        for name in value:
            avg += elo_points_for_player
        
        print("{} ({}) {:.1f}".format(key, len(value), (avg/len(value))))
        


        for name in value:
            print("{:>40}{:>10}".format(name, elo_points_for_player))




def main():
    file_name = get_filename_from_user("Enter name of file: ")

    chess_player_data = get_data_from_file(file_name)

    country_dict = create_country_dict(chess_player_data)

    print_header("Players by country:")
    
    print_resault(chess_player_data, country_dict)


main()

