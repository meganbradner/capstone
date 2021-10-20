const App = {
    
    delimiters: ['[[', ']]'],

    data() {

        return  {
            userBook: '',
            userAuthor: '',
            foundBooks: null,
            foundAuthors: null
        }
    },

    methods: {
        
        findBook() {
            axios({
                method: 'get',
                url: `https://www.googleapis.com/books/v1/volumes?q=${this.userBook}`,
            }).then(response => {
                console.log(response.data)
                this.foundBooks = response.data
                
                all_books = {}
                for (let i = 0; length(); i++) {
                    book_data = Book(
                        title = i['title'],
                        author = i['authors'],
                        description = i['description'],
                        image = i['imageLinks']

                    )
                }
            })
        },

        findAuthor() {
            axios({
                method: 'get',
                url: `https://www.googleapis.com/books/v1/volumes?q=${this.userAuthor}`,
                // params: {
                //     q: this.userAuthor
                // },
            }).then(response => {
                console.log(response.data.items[0].volumeInfo)
                this.foundAuthors = response.data.items[0].volumeInfo

            })
        },

    }

}
Vue.createApp(App).mount('#app')

