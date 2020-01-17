<template>
    <div class="Admin">
        <Navbar></Navbar>
        
        <div class="container">
            <br><br><br>
            <h2>Administration</h2>
            <br><br>
            <p v-if="message">{{message}}</p>
            <p v-if="res_op">{{res_op}}</p>

            <div class="col-md-8 offset-md-2" style="text-align: center;">
                <div v-for="user in users">
                    <span>
                        <strong>{{user.username}}</strong>
                    </span>
                    <button v-if="user.username != 'admin'" type="button" class="btn btn-danger mbtn btnl" @click="remove_user(user)">Delete</button>
                    <br><br>
                </div>
            </div>
            
        </div>
    </div>
</template>

<script>

import Navbar from './Navbar'

export default {
    name: "Admin",
    components: {
        Navbar,
    },
    data () {
        return {
            datas: null,
            users: null,
            message: null,
            res_op: null,
        }
    },
    methods: {
        get_users: function() {
            this.$http.get('http://localhost:5005/users',
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    this.datas = response.data;
                    if (this.datas.status == "success") {
                        this.users = this.datas.datas;
                        this.message = null;
                    } else
                        this.message = this.datas.message;
                }, (error) => {
                    this.message = "Error";
                });
        },
        remove_user: function(user) {
            this.$http.delete('http://localhost:5005/user/'+user.id.toString(),
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    if (response.data.status == "success") {
                        this.get_users();
                        this.res_op = "User '"+user.username+"' successfully deleted";
                    } else
                        this.res_op = response.data.message;
                }, (error) => {
                    this.res_op = "Error";
                });
        }
    },
    beforeMount(){
        this.get_users();
    }
}
</script>
<style scoped>
</style>