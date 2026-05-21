# Mapping Examples

## Order Submission

DDD input:

- Command: 提交订单
- Event: 订单已提交
- Aggregate: 订单
- Invariant: 库存不足时不能提交
- Read model: 订单详情

TDD slices:

1. 提交有效订单会产生 `订单已提交`
   - Test layer: aggregate or application service
   - RED: no event is produced for a valid command
   - GREEN: command handler validates state and records the event

2. 库存不足时提交失败
   - Test layer: aggregate unit test
   - RED: insufficient stock still allows submission
   - GREEN: invariant blocks submission and no submitted event is emitted

3. 订单已提交后订单详情可查询
   - Test layer: projection/query test
   - RED: projection does not create or update order details
   - GREEN: `订单已提交` updates the read model

## Policy Mapping

DDD input:

- Event: 月度考勤已结算
- Policy: 满勤奖励策略
- Command: 发放满勤奖励

TDD slice:

- 月度考勤已结算且员工满勤时触发发放满勤奖励
- Test layer: policy/orchestration test
- RED: event does not produce the command
- GREEN: policy subscribes to the event and emits the command with the required fields
