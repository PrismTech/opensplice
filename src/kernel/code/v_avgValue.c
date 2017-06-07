/*
 *                         OpenSplice DDS
 *
 *   This software and documentation are Copyright 2006 to TO_YEAR PrismTech
 *   Limited, its affiliated companies and licensors. All rights reserved.
 *
 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at
 *
 *       http://www.apache.org/licenses/LICENSE-2.0
 *
 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 *
 */
 
#include "v_avgValue.h"

void
v_avgValueInit(
    v_avgValue *_this)
{
    assert(_this != NULL);
    v_avgValueReset(_this);
}

void
v_avgValueReset(
    v_avgValue *_this)
{
    assert(_this != NULL);
    _this->count = 0;
    _this->value = 0.0;
}

c_float
v_avgValueGetValue(
    v_avgValue *_this)
{
    assert(_this != NULL);
    return _this->value;
}

void
v_avgValueSetValue(
    v_avgValue *_this, 
    c_ulong value)
{
    double delta;

    _this->count++;
    delta = ((double)value - _this->value) / _this->count;
    _this->value += (c_float) delta;
}

