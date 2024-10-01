from collections import defaultdict
def solution(genres, plays):
    answer = []
    
    genre_dict = defaultdict(list)
    genre_played = defaultdict(int)
    
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        genre_dict[genre].append((play, i))
        genre_played[genre] += play
        
    sorted_genres = sorted(genre_played.items(), key=lambda k:k[1], reverse=True)
    # print(sorted_genres)
    
    for tmp in sorted_genres:
        genre = tmp[0]
        sorted_plays = sorted(genre_dict[genre], key=lambda k:(k[0], -k[1]), reverse=True)
        # print(sorted_plays)
        for play in sorted_plays[:min(2, len(sorted_plays))]:
            answer.append(play[1])
    
    
    return answer
