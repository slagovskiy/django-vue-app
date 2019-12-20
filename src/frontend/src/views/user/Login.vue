<template>
    <div class="text-center">
        <b-form v-on:submit.prevent="onSubmit" v-on:reset.prevent="onReset" class="form-signin">
            <img class="mb-4" src="/static/img/logo.gif" alt="" width="80" height="80">
            <h1 class="h3 mb-3 font-weight-normal">Please sign in</h1>
            <b-form-group
                id="input-group-1"
                label=""
                label-for="email"
                description=""
            >
                <b-form-input
                    id="email"
                    v-model="form.email"
                    type="text"
                    required
                    placeholder="Enter email"
                ></b-form-input>
            </b-form-group>
            <b-form-group
                id="input-group-2"
                label=""
                label-for="password"
                description=""
            >
                <b-form-input
                    id="password"
                    v-model="form.password"
                    type="password"
                    required
                    placeholder="Enter password"
                ></b-form-input>
            </b-form-group>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
            <div class="link">or <a href="#">Register</a></div>
        </b-form>
    </div>
</template>

<script>
    import globalMixin from '../../mixins/global'
    import userMixin from '../../mixins/user'

    // eslint-disable-next-line
    var reEmail = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/

    export default {
        mixins: [globalMixin, userMixin],
        data() {
            return {
                form: {
                    email: 'slagovskiy@gmail.com',
                    password: '123qwe'
                }
            }
        },
        computed: {
        },
        methods: {
            onSubmit() {
                console.log(this.form)
                //if (this.$refs.form.validate()) {
                    this.$store.dispatch('login', this.form)
                        .then(() => {
                            console.log(this.$store.getters.jwt)
                            if (this.$store.getters.jwt!='') {
                                this.$router.push({name: 'userAutoLogin'})
                            }
                        })
                        .catch(() => {
                        });
                //}
            },
            onReset() {
                this.form = {
                    email: '',
                    password: ''
                }
            },
            restorePassword() {
                //this.$router.push({name: 'user-restore'});
            }
        }
    }
</script>

<style scoped>
    .form-signin {
        width: 100%;
        max-width: 330px;
        padding: 15px;
        margin: auto;
    }

    .form-group {
        margin-bottom: 0;
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

    .form-signin input[id="username"] {
        margin-bottom: -1px;
        border-bottom-right-radius: 0;
        border-bottom-left-radius: 0;
    }

    .form-signin input[id="password"] {
        margin-bottom: 10px;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }

    .form-signin .link {
        padding-top: 10px;
    }
</style>
