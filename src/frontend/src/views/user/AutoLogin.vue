<template>
    <div class="block-center">
        <b-spinner type="grow" label="Spinning"></b-spinner>
        <b-spinner type="grow" label="Spinning"></b-spinner>
        <b-spinner type="grow" label="Spinning"></b-spinner>
    </div>
</template>

<script>
    export default {
        mounted: function () {
            this.$nextTick(function () {
                this.$store.dispatch('autoLogin')
                    .then(() => {
                        if (!this.error) {
                            if (this.$route.query['redirect'])
                                this.$router.push(this.$route.query['redirect'])
                            else
                                this.$router.push({name: 'userProfile'})
                        }
                    })
            })
        }
    }
</script>

<style scoped>
    .block-center {
        position: absolute;
        top: 50%;
        left: 50%;
        margin-right: -50%;
        transform: translate(-50%, -50%)
    }

    .block-center span {
        margin-left: 10px;
        margin-right: 10px;
    }
</style>