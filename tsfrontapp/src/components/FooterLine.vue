<template>
    <footer>
        <div class="top-line"></div>
        <ul class="footer-list">
            <li>
                <a class="footer-link">客服中心</a>
            </li>
            <li>
                <a class="footer-link">关于我们</a>
            </li>
        </ul>
    </footer>
</template>

<script lang="ts" setup name="Footer"></script>

<style scoped>

footer {
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100px;
    width: 100%;
    background-color: rgb(190, 226, 240);
}

.top-line {
    display: flex;
    height: 5px;
    width: 100%;
    background: linear-gradient(to right, rgb(190, 226, 240), #fff, rgb(190, 226, 240));
}

.footer-list {
    height: 100%;

    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: #555;

    list-style: none;
}


.footer-list li {
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;

    list-style: none;
}

footer > li:hover {
    cursor: pointer;
}

.footer-link {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 100%;
    padding: 0 20px;
    color: #555;
}

.footer-link:hover {
    cursor: pointer;
    color: #000;
}


</style>
