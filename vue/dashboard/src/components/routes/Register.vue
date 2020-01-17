<template>
    <div class="Register">
        <!-- <p>{{ counter }}</p>
        <button @click="increase">UP</button> -->
        
        <div class="main text-center">
            <form class="form-signin" v-on:submit.prevent="logUser">
            <img class="mb-4" src="../../assets/dashboard.png" alt="" width="90" height="90">
            <p v-if="message">{{message}}</p>
            <h1 class="h3 mb-3 font-weight-normal">Register</h1>
            <input v-model="username" type="text" id="inputEmail" class="form-control" placeholder="Username" required autofocus>
            <input v-model="mail" type="text" id="inputPassword2" class="form-control" placeholder="Mail" required>
            <input v-model="password" type="password" id="inputPassword" class="form-control" placeholder="Password" required>
            <button class="btn btn-lg btn-primary btn-block">Register</button>
            <br>
            <router-link to="/Login">Login</router-link>
            </form>
        </div>

    </div>
</template>

<script>
export default {
    name: "Register",
    data () {
        return {
            counter: 0,
            username: null,
            password: null,
            request: null,
            message: null,
            mail: null
        }
    },
    methods: {
        logUser: function() {
            this.$http.post('http://localhost:5005/register', {
                username: this.username,
                password: this.password,
                mail: this.mail,
                })
                .then((response) => {
                    if (response.data.status == "error")
                        this.message = response.data.message;
                    else if (response.data.status == "success")
                        this.message = "Successful registration";
                }, (error) => {
                    this.message = "Bad password or username.";
                });
        }
    }
}

</script>
<style scoped>
.main {
  height: 100%;
}

.main {
  display: -ms-flexbox;
  display: -webkit-box;
  display: flex;
  -ms-flex-align: center;
  -ms-flex-pack: center;
  -webkit-box-align: center;
  align-items: center;
  -webkit-box-pack: center;
  justify-content: center;
  padding-top: 40px;
  padding-bottom: 40px;
}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}

.form-control {
    margin-bottom: 5px;
}

</style>