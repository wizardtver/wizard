import { SortOrder } from "../../util/SortOrder";

export type ReviewOrderByInput = {
  id?: SortOrder;
  createdAt?: SortOrder;
  updatedAt?: SortOrder;
  rating?: SortOrder;
  reviewText?: SortOrder;
  userId?: SortOrder;
  productId?: SortOrder;
};
