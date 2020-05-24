<template>
    <div class="container">
        <div class="row">
            <div class="col-sm-10">
                <h1>Tasks</h1>
                <br><br>
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th scope="col">Title</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(task, index) in tasks" :key="index">
                            <td>{{ task.title }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div>
            <b-form @submit="onSubmit" @reset="onReset">
                <b-form-group id="input-group-1" label="Add Task" label-for="input-1">
                    <b-form-input id="input-1" v-model="form.task" type="text" required placeholder="Enter task"></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return {
            tasks: [],
            form: {
                task: '',
            }
        }
    },
    methods: {
        getTasks() {
            const path = 'http://localhost:5000/tasks';
            axios.get(path).then((res) => {
                console.log(res)
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.error(error);
            })
        },
        onSubmit(evt) {
            evt.preventDefault();
            const path = 'http://localhost:5000/tasks';
            let payload = {'task': this.form.task};
            console.log(payload);
            axios.post(path, payload).then((res) => {
                this.tasks = res.data.tasks;
            }).catch((error) => {
                console.error(error);
            })
        },
        onReset(evt) {
            evt.preventDefault();
            this.form.task = '';
        }
    },
    created() {
        this.getTasks();
    }
};
</script>