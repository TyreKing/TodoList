<template>
  <div class="container">
    <div class="content">
      <h1>Todo</h1>
      <ul>
        <li v-for="item in todolist" :key="item.id">
          {{ item.description }}
          <input type="checkbox" id="checkbox" v-model="checked" />
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      todolist: [] 
    };
  },
  created() {
    this.fetchData();
  },
  methods:{
    fetchData() {
      axios.get('http://127.0.0.1:5000/api/todo')
      .then(response => {
        this.todolist = response.data;
      })
      .catch(error => {
        console.error('Error fetching todo list', error);
      })
    }
  }
};
</script>

<style>
.continater {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.content {
  background-color: rgba(0, 0, 0, 0.103);
  border-radius: 10px;
  padding: 20px;
}

li {
  list-style-type: none;
}
</style>