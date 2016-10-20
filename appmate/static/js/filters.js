import moment from 'moment'

export default {
  timeago(val /* Timestamp */) {
    return moment(val * 1000).fromNow()
  },
  json(val) {
    return JSON.stringify(val, null, 2)
  },
}
