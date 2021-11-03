const App = {

    delimiters: ['[[', ']]'],

    data() {

        return {
            userBook: '',
            userAuthor: '',
            newBook: '',
            csrfmiddlewaretoken: '',
            foundBooks: null,
            foundAuthors: null,
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
            })
        },

        currentlyReading() {
            axios({
                method: 'post',
                url: '/add-current',
                data: {
                    title: this.foundBooks.items[0].volumeInfo.title,
                    author: this.foundBooks.items[0].volumeInfo.authors,
                    image: this.foundBooks.items[0].volumeInfo.imageLinks.thumbnail
                },
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            }).then(response => this.findBook())

        },

        alreadyRead() {
            axios({
                method: 'post',
                url: '/add-read',
                data: {
                    title: this.foundBooks.items[0].volumeInfo.title,
                    author: this.foundBooks.items[0].volumeInfo.authors,
                    image: this.foundBooks.items[0].volumeInfo.imageLinks.thumbnail,
                },
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            }).then(response => this.findBook())
        },

        wantToRead() {
            axios({
                method: 'post',
                url: '/add-want',
                data: {
                    title: this.foundBooks.items[0].volumeInfo.title,
                    author: this.foundBooks.items[0].volumeInfo.authors,
                    image: this.foundBooks.items[0].volumeInfo.imageLinks.thumbnail
                },
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            }).then(response => this.findBook())
        },


        // findAuthor() {
        //     axios({
        //         method: 'get',
        //         url: `https://www.googleapis.com/books/v1/volumes?q=${this.userAuthor}`,
        //     }).then(response => {
        //         console.log(response.data)
        //         this.foundAuthors = response.data.items

        //     })
        // }

    },
    mounted() {
        this.csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
    }

}
Vue.createApp(App).mount('#app')

