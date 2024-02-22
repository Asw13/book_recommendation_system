from flask import Flask,render_template,request
import pickle
import numpy as np

popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
pt1 = pickle.load(open('pt1.pkl','rb'))
pt2 = pickle.load(open('pt2.pkl','rb'))
pt5 = pickle.load(open('pt5.pkl','rb'))
books = pickle.load(open('book.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))
similarity_scores1 = pickle.load(open('similarity_scores1.pkl','rb'))
similarity_scores2 = pickle.load(open('similarity_scores2.pkl','rb'))
your_years_list=list(books['Year_Of_Publication'].dropna().unique())
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home1.html',
                           book_name = list(popular_df['Book_Title'].values),
                           author=list(popular_df['Book_Author'].values),
                           image=list(popular_df['Image_URL_M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values),
                           your_years_list=list(books['Year_Of_Publication'].dropna().unique())
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:3]

    data11 = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book_Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Book_Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Book_Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Image_URL_M'].values))

        data11.append(item)

    index = np.where(pt1.index== user_input)[0][0]
    similar_items1 = sorted(list(enumerate(similarity_scores1[index])),key=lambda x:x[1],reverse=True)[1:3]
    
    data12 = []
    for i in similar_items1:
        item1 = []
        temp_df1 = books[books['Book_Title'] == pt1.index[i[0]]]
        item1.extend(list(temp_df1.drop_duplicates('Book_Title')['Book_Title'].values))
        item1.extend(list(temp_df1.drop_duplicates('Book_Title')['Book_Author'].values))
        item1.extend(list(temp_df1.drop_duplicates('Book_Title')['Image_URL_M'].values))
        
        data12.append(item1)
    
    index = np.where(pt2.index== user_input)[0][0]
    similar_items2 = sorted(list(enumerate(similarity_scores2[index])),key=lambda x:x[1],reverse=True)[1:3]
    
    data13 = []
    for i in similar_items2:
        item2 = []
        temp_df2 = books[books['Book_Title'] == pt2.index[i[0]]]
        item2.extend(list(temp_df2.drop_duplicates('Book_Title')['Book_Title'].values))
        item2.extend(list(temp_df2.drop_duplicates('Book_Title')['Book_Author'].values))
        item2.extend(list(temp_df2.drop_duplicates('Book_Title')['Image_URL_M'].values))
        
        data13.append(item2)
    
    print(data11,data12,data13)

    
    

    return render_template('recommend.html',data=data11,data1=data12,data2=data13)

@app.route('/books/<int:year>')

def books_by_year(year):
    
    #popular_df = popular_df[popular_df['num_ratings']>=250].sort_values('avg_rating',ascending=False).head(10)
    # index fetch
    index = np.where(pt5.columns==year)[0][0]
    sorted_dataframe = pt5.sort_values(by=year, ascending=False).index[:10]
    

    data = []
    for i in sorted_dataframe :
        
        item = []
        temp_df = books[books['Book_Title'] ==i] 
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Book_Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Book_Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book_Title')['Image_URL_M'].values))
        item
        
        data.append(item)
        
    
    return render_template('your_template.html', release_years=your_years_list, top_books=data)





if __name__ == '__main__':
    app.run(debug=True)