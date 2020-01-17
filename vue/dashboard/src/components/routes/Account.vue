<template>
    <div class="Account">
        <Navbar></Navbar>
        <br>

        <div class="container">
            <br><br><br><br><br>
            <div class="row">
                <div class="col-md-6 offset-md-3">
                
                <h3>{{username}}</h3>
                <br>
                <div v-if="message">
                    <p>{{message}}</p>
                </div>

                <div class="input-group mb-2">
                    <div class="input-group-prepend">
                        <span class="input-group-text">Mail</span>
                    </div>
                    <input v-model="mail" class="form-control" type="text" placeholder="Username">
                </div>
                
                <div class="input-group mb-2">
                    <div class="input-group-prepend">
                        <span class="input-group-text">Password</span>
                    </div>
                    <input v-model="password" class="form-control" type="password">
                </div>
                <br>
                <button @click="update_infos" type="button" class="btn btn-success mbtn">Update</button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>

import Navbar from './Navbar';

export default {
    name: "Account",
    components: {
        Navbar,
    },
    data () {
        return {
            mail: null,
            username: null,
            password: null,
            send_datas: {},
            message: null,
            datas: null,
        }
    },
    methods: {
        get_infos: function() {
            this.$http.get('http://localhost:5005/user', {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    this.datas = response.data;
                    this.mail = this.datas.mail;
                    this.username = this.datas.username;
                }, (error) => {
                    this.message = "Error";
                });
        },
        update_infos: function() {
            this.send_datas['mail'] = this.mail;
            if (this.password)
                this.send_datas['password'] = this.password
            this.$http.put('http://localhost:5005/user', this.send_datas,
            {headers: {'Authorization': "JWT "+localStorage.access_token}})
                .then((response) => {
                    if (response.data.status == "success") {
                        this.message = response.data.message;
                        this.get_infos();
                    } else
                        this.message = "Error";
                }, (error) => {
                    this.message = "Error";
                });
            this.password = null;
            this.send_datas = {};
        }
    },
    beforeMount(){
        this.get_infos();
    },
}
</script>
<style scoped>
</style>