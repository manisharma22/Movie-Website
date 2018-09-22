import media
import fresh_tomatoes

avengers = media.Movie("The Avengers","S.H.I.E.L.D. leader Nick Fury is compelled to launch the Avengers Initiative when Loki poses a threat to planet Earth. His squad of superheroes put their minds together to accomplish the task.","https://www.google.co.in/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/8815512/p8815512_v_v8_an.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DMarvel%2527s%2Bthe%2BAvengers&h=1440&w=960&tbnid=Zf4ZsRLPxsGpQM:&q=The+Avengers&tbnh=186&tbnw=124&usg=AI4_-kTSwf33K_H3rWqDIxjIR5wthI8-7g&vet=12ahUKEwiBrNniz87dAhUObisKHWXjAYIQ_B0wG3oECAcQCQ..i&docid=LXQYS2EJ4b60iM&itg=1&sa=X&ved=2ahUKEwiBrNniz87dAhUObisKHWXjAYIQ_B0wG3oECAcQCQ","https://www.youtube.com/watch?v=kq84NymZYJE")
captain_america = media.Movie("Captain America: Civil War","Friction arises between the superheroes when one group supports the government's decision to implement a law to control their powers while the other opposes it.","https://www.google.co.in/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/10989225/p10989225_v_v8_ax.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DCaptain%2BAmerica:%2BCivil%2BWar&h=1440&w=960&tbnid=8Eh2SDzQImyZvM:&q=Captain+America:+Civil+War&tbnh=186&tbnw=124&usg=AI4_-kQFv5AkKOlfZq9Ic_IyL_wv80FCog&vet=12ahUKEwj08_iy0M7dAhUSfSsKHf0pCUgQ_B0wH3oECAQQCQ..i&docid=fjesh6au1f2g4M&itg=1&sa=X&ved=2ahUKEwj08_iy0M7dAhUSfSsKHf0pCUgQ_B0wH3oECAQQCQ","https://www.youtube.com/watch?v=pD9fr686QfA")
black_panther = media.Movie("Black Panther","After the death of his father, T'Challa returns home to the African nation of Wakanda to take his rightful place as king. When a powerful enemy suddenly reappears, T'Challa's mettle as king ","https://www.google.co.in/imgres?imgurl=http://www.gstatic.com/tv/thumb/v22vodart/12878741/p12878741_v_v8_ac.jpg&imgrefurl=http://google.com/search?tbm%3Disch%26q%3DBlack%2BPanther&h=1440&w=960&tbnid=plA2uUTSfGupUM:&q=Black+Panther&tbnh=186&tbnw=124&usg=AI4_-kRq1lA2leAkmyGfzXe9BMDGgFG9Sw&vet=12ahUKEwjwqN3w0M7dAhVHVH0KHb1OBiEQ_B0wIHoECAYQCQ..i&docid=2ApP3AXel5kEkM&itg=1&sa=X&ved=2ahUKEwjwqN3w0M7dAhVHVH0KHb1OBiEQ_B0wIHoECAYQCQ","https://www.youtube.com/watch?v=KBPp155Fqa8")

movies = [avengers,captain_america,black_panther]
fresh_tomatoes.open_movies_page(movies)



