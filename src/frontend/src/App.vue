<template>
    <div>
        <router-view/>
        <footer class="footer">
            <div class="container">
                <p class="text-muted">Django vue app &copy; 2019</p>
            </div>
        </footer>
    </div>
</template>

<style>
    html,
    body {
        height: 100%;
    }

    html {
        position: relative;
        min-height: 100%;
    }

    body {
        margin-bottom: 60px; /* Margin bottom by footer height */
        background-color: #f5f5f5 !important;
    }

    .footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 60px; /* Set the fixed height of the footer here */
        padding-top: 18px;
        border-top: 1px solid #DDDDDD;
        background-color: #f5f5f5;
        font-size: 0.8em;
        text-align: center;
    }
</style>
