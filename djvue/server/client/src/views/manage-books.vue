<template>
  <div class="container-fluid">
    <Loading :msg="message" v-if="loading"></Loading>
    <div class="row" v-show="!loading">
      <div class="col-sm-12" v-show="books.length">
        <h2>Libri disponibili {{books.length}}</h2>
      </div>
    </div>
    <div class="form-row" v-show="!loading">
      <div class="col-lg-6 mb-2 flex-column" v-for="book in books" :key="book.id">
        <div class="card h-100">
          <div class="card-header d-flex">
            <h4
              class="text-truncate flex-grow-1 flex-shrink-1 mb-0 pb-1 align-self-center"
              :title="book.book_name"
            >{{book.book_name}}</h4>
            <button
              class="btn btn-lg btn-link flex-grow-0 flex-shrink-0"
              @click="askToDelete(book)"
            >Delete book</button>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-sm-12">{{book.plot}}</div>
              <div class="col-lg-6">
                <label>ISBN</label>
                {{book.isbn}}
              </div>
              <div class="col-lg-6">
                <label>Copies disponibili</label>
                {{book.copies_available}}
              </div>
              <div class="col-lg-6">
                <label>ISBN</label>
                {{book.ISBN}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ManageBooks',
  data() {
    return {
      books:null,
      url:'',
      title:'',
      body:'',
      csrf: ''
    };
  },
  mounted(){
    this.getAll();
  },
  methods: {
    getAll(){
      axios.get('http://localhost:8000/books').then((res)=>{
          this.books=res.data;
          this.url='';
          this.title='';
          this.plot='';
      })
    }, 
    getOne(book){
      this.url=book.id;
      this.title=book.title;
      this.body=book.body;
    },
    askToDelete(url){
      axios.delete(url,{auth:{
            username:'admin',
            password: 'admin'
          }})
      .then(()=>{
          this.getAll();
        })
    }   
  }
}
</script>
<style scoped lang="scss">
.card {
  min-height: 150px;
}
</style>